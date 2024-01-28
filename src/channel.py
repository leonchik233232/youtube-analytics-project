from googleapiclient.discovery import build
import json
class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'AIzaSyAMpe-6QlikT2WeOmeWlXBS3Gt3sVTuR4A'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.get_channel_info()

    def get_channel_info(self):
        channel_info = self.youtube.channels().list(
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
        api_key = 'YT_API_KEY'
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, file_name):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(file_name, 'w') as file:
            json.dump(data, file)

    def print_info(self):
        channel_info = self.youtube.channels().list(
            part='snippet, statistics',
            id=self.channel_id
        ).execute()

        print(json.dumps(channel_info, indent=2, ensure_ascii=False))