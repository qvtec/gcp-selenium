from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ChromeClass:
    def __init__(self, driver=""):
        self.driver = driver

    def create_driver(self, binary_location):
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--no-sandbox")
        options.add_argument("--hide-scrollbars")

        options.add_argument('--headless')
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--v=99")
        options.add_argument('--disable-logging')
        options.add_argument("--single-process")

        self.driver = webdriver.Chrome(options=options)

    def quit(self) -> None:
        self.driver.quit()

    def get(self, url) -> None:
        self.driver.get(url)
        print(self.driver.title)

    def input(self, value, name, by=By.ID) -> None:
        input_box = self.driver.find_element(by, name)
        input_box.send_keys(value)

    def select(self, value, name, by=By.ID) -> None:
        dropdown = self.driver.find_element(by, name)
        Select(dropdown).select_by_value(value)

    def click(self, name, by=By.ID) -> None:
        btn = self.driver.find_element(by, name)
        btn.click()

    def submit(self, name, by=By.ID) -> None:
        btn = self.driver.find_element(by, name)
        btn.submit()