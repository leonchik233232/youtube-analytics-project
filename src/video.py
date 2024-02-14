import requests

class Video:
    def __init__(self, video_id):
        try:
            response = requests.get(f"https://youtube.com/watch?v={video_id}")
            if response.status_code != 200:
                raise ValueError("Invalid video ID")

            soup = BeautifulSoup(response.content, "html.parser")
            self.title = soup.find("title").text
            self.url = f"https://youtube.com/watch?v={video_id}"
            self.view_count = int(soup.find("div", class_="view-count").text.split()[0].replace(",", ""))
            self.like_count = int(soup.find("button", class_="like-button-renderer-like-button").text.split()[0])
        except (ValueError, AttributeError):
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
