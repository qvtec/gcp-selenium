from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClass:
    def __init__(self, token, channelId):
        self.client = WebClient(token=token)
        self.CHANNEL_ID = channelId

    def send(self, message, file=""):
        try:
            if not file:
                response = self.client.chat_postMessage(
                    channel=self.CHANNEL_ID,
                    text=message
                )
            else:
                response = self.client.files_upload_v2(
                    channel=self.CHANNEL_ID,
                    initial_comment=message,
                    file=file,
                    title="Image"
                )

            if response["ok"]:
                print("Slack送信")
            else:
                print(f"Slack送信失敗: {response['error']['msg']}")

        except SlackApiError as e:
            print(f"Slack APIエラー: {e.response['error']}")
