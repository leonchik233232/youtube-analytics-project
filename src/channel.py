from googleapiclient.discovery import build

class Channel:
    def init(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'YOUR_API_KEY'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self):
        channel_info = self.youtube.channels().list(
            part='snippet, statistics',
            id=self.channel_id
        ).execute()

        channel = channel_info['items'][0]

        title = channel['snippet']['title']
        description = channel['snippet']['description']
        view_count = channel['statistics']['viewCount']
        subscriber_count = channel['statistics']['subscriberCount']
        video_count = channel['statistics']['videoCount']

        print('Title: ', title)
        print('Description: ', description)
        print('View Count: ', view_count)
        print('Subscriber Count: ', subscriber_count)
        print('Video Count: ', video_count)
