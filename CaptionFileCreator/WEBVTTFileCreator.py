from CaptionFileCreator.CaptionFileCreator import CaptionFileCreator
from typing import override
from Models.Caption import Caption
from utils.FilePathManager import FilePathManager

class WEBVTTFileCreator(CaptionFileCreator):
    # @override
    def __init__(self, language: str, tv_show: str, season: int, episode: int, filePathManager: FilePathManager):
        super().__init__(language, tv_show, season, episode, filePathManager)
        self.file_header = f"""WEBVTT - {self.description}
                           """
        self.file_extension = ".vtt"

    @override
    @staticmethod
    def convert_caption(caption: Caption) -> str:
        return caption.to_webvtt_text()
