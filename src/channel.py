from googleapiclient.discovery import build
import json
import os
YT_API_KEY = os.getenv('YT_API_KEY')

class Channel:
    def init(self, channel_id):
        self.channel_id = channel_id
        self.title = self.get_title()
        self.description = self.get_description()
        self.url = self.get_url()
        self.subscriber_count = self.get_subscriber_count()
        self.video_count = self.get_video_count()
        self.view_count = self.get_view_count()

    def get_title(self):
        service = self.get_service()
        response = service.channels().list(
            part='snippet',
            id=self.channel_id
        ).execute()
        return response['items'][0]['snippet']['title']

    def get_description(self):
        service = self.get_service()
        response = service.channels().list(
            part='snippet',
            id=self.channel_id
        ).execute()
        return response['items'][0]['snippet']['description']

    def get_url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    def get_subscriber_count(self):
        service = self.get_service()
        response = service.channels().list(
            part='statistics',
            id=self.channel_id
        ).execute()
        return int(response['items'][0]['statistics']['subscriberCount'])

    def get_video_count(self):
        service = self.get_service()
        response = service.channels().list(
            part='statistics',
            id=self.channel_id
        ).execute()
        return int(response['items'][0]['statistics']['videoCount'])

    def get_view_count(self):
        service = self.get_service()
        response = service.channels().list(
            part='statistics',
            id=self.channel_id
        ).execute()
        return int(response['items'][0]['statistics']['viewCount'])

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=YT_API_KEY)

    def to_json(self, file_name):
        data = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file_name, 'w') as file:
            json.dump(data, file)
