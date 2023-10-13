import base64
import time
import os

from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

from lib.chrome import ChromeClass
from lib.slack import SlackClass

import functions_framework

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def handler(cloud_event):
    print('=== Start ===')
    # Print out the data from Pub/Sub, to prove that it worked
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    main()
    print('=== End ===')


def main():
    chrome = ChromeClass()
    chrome.create_driver(os.getenv("CHROME_DRIVER_PATH"))
    chrome.get('https://www.google.com/')
    chrome.input('ChromeDriver', 'q', By.NAME)
    chrome.submit('q', By.NAME)
    time.sleep(1)

    FILE_PATH = os.getenv("FILE_PATH")
    chrome.driver.save_screenshot(FILE_PATH)
    chrome.quit()

    SLACK_TOKEN = os.getenv("SLACK_TOKEN")
    SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

    slack = SlackClass(SLACK_TOKEN, SLACK_CHANNEL_ID)
    slack.send("OK!", FILE_PATH)


#------------------------------------------------------------------------
# 実行
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
