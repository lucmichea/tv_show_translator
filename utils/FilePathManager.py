import os
from utils.FileType import FileType

class FilePathManager(object):
    DOWNLOAD_FOLDER = "_shows"

    def __init__(self, 
                 tv_show: str, 
                 season: int, 
                 episode: int,
                 sub_extension: str,
                 root_path: str):
        self.tv_show = tv_show
        self.season = season
        self.episode = episode
        self.sub_extension = sub_extension  # File extension for subtitle files (e.g., srt, vtt)  # File extension for subtitle files (e.g., srt, vtt)  # File extension for subtitle files (e.g., srt, vtt)
        self.root_path = root_path
        self.download_path = os.path.join(self.root_path, 
                                          self.DOWNLOAD_FOLDER, 
                                          self.tv_show, 
                                          f"season_{self.season}")

    def get_download_path(self) -> str:
        return self.download_path

    def get_file_path(self, filetype: FileType) -> str:
        match filetype:
            case FileType.VIDEO:
                return os.path.join(self.download_path, f"episode_{self.episode}.mp4")
            case FileType.AUDIO:
                return os.path.join(self.download_path, f"episode_{self.episode}.mp3")
            case FileType.JSON:
                return os.path.join(self.download_path, f"episode_{self.episode}.json")
            case FileType.CAPTION:
                return os.path.join(self.download_path, f"episode_{self.episode}.{self.sub_extension}")
            case FileType.COMBINED: 
                return os.path.join(self.download_path, f"episode_{self.episode}.mkv")
            case _:
                raise ValueError("Unsupported file type")
