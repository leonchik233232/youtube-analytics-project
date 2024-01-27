from googleapiclient.discovery import build
import json
class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'YOUR_API_KEY'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self):
        channel_info = self.youtube.channels().list(
            part='snippet, statistics',
            id=self.channel_id
        ).execute()

        print(json.dumps(channel_info, indent=2, ensure_ascii=False))