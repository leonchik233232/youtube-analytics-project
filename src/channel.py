from googleapiclient.discovery import build
import os
class Channel:
    def __init__(self, channel_id):
        api_key: str = os.getenv('YT_API_KEY')
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_info(self):
        request = self.youtube.channels().list(
            part='statistics',
            id=self.channel_id
        )
        response = request.execute()
        statistics = response['items'][0]['statistics']

        info_dict = {
            'Channel ID': self.channel_id,
            'Subscriber count': statistics['subscriberCount'],
            'View count': statistics['viewCount'],
            'Video count': statistics['videoCount']
        }

        return info_dict
