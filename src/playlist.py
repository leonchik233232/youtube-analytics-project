from dataclasses import dataclass, field
import datetime
from typing import List

@dataclass
class Video:
    title: str
    link: str
    duration: datetime.timedelta
    likes: int = 0

    def __repr__(self):
        return f"{self.title} ({self.duration}, {self.likes} likes)"


@dataclass
class PlayList(Video):
    playlist_id: str
    videos: List[Video] = field(default_factory=list)

    @property
    def total_duration(self) -> datetime.timedelta:
        return sum(video.duration for video in self.videos)

    def show_best_video(self) -> Video:
        return max(self.videos, key=lambda video: video.likes)