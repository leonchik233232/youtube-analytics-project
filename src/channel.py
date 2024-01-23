import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = "AIzaSyC3adqgbkITK7mjmYywl2kAOp5NuaT3ZXE"
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()

        channel_data = data["items"][0]
        title = channel_data["snippet"]["title"]
        description = channel_data["snippet"]["description"]
        view_count = channel_data["statistics"]["viewCount"]
        subscriber_count = channel_data["statistics"]["subscriberCount"]
        video_count = channel_data["statistics"]["videoCount"]

        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"View Count: {view_count}")
        print(f"Subscriber Count: {subscriber_count}")
        print(f"Video Count: {video_count}")
        pass