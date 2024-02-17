from googleapiclient.discovery import build

class Video:
    def __init__(self, video_id):
        youtube = build("youtube", "v3", developerKey="YOUR_API_KEY")

        try:
            response = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id
            ).execute()

            video_data = response["items"][0]

            self.title = video_data["snippet"]["title"]
            self.url = f"https://youtube.com/watch?v={video_id}"
            self.view_count = video_data["statistics"]["viewCount"]
            self.like_count = video_data["statistics"]["likeCount"]
        except (ValueError, AttributeError):
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

