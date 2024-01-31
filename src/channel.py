from googleapiclient.discovery import build
import json
import os

class Channel:
    def __init__(self, channel_id):
        self._channel_id = channel_id
        self.get_channel_info()

    @property
    def channel_id(self):
        return self._channel_id

    def get_channel_info(self):
        channel_info = self.get_service().channels().list(
            part='snippet, statistics',
            id=self.channel_id
        ).execute()

        self.id = channel_info['items'][0]['id']
        self.title = channel_info['items'][0]['snippet']['title']
        self.description = channel_info['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.id}"
        self.subscriber_count = channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = channel_info['items'][0]['statistics']['videoCount']
        self.view_count = channel_info['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        channel_info = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, "w") as file:
            json.dump(channel_info, file, ensure_ascii=False, indent=2)

    def print_info(self):
        channel_info = self.get_service().channels().list(
            part='snippet, statistics',
            id=self.channel_id
        ).execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))
