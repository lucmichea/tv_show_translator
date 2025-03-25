import os
from typing import List
from Models.Caption import Caption
from utils.FilePathManager import FilePathManager
from utils.FileType import FileType

class CaptionFileCreator(object):

    def __init__(self, language: str, tv_show: str, season: int, episode: int, filePathManager: FilePathManager):
        self.filePathManager = filePathManager
        self.description = f"{language} Caption for {tv_show} season_{season} episode_{episode}"
        self.captions: List[Caption] = []
        self.file_payload = ""
        self.file_header = """
                           """

    def add_caption(self, caption: Caption):
        self.captions.append(caption)

    def sort_captions(self) -> None:
        self.captions.sort(key=lambda x: x.start_time)

    # Override this method based on the File Type you are working with.
    @staticmethod
    def convert_caption(caption: Caption) -> str:
        pass

    def create_caption_file(self) -> None:
        self.file_payload += self.file_header
        self.sort_captions()
        for caption in self.captions:
            self.file_payload += self.convert_caption(caption)
        
        with open(self.filePathManager.get_file_path(FileType.CAPTION), "w", encoding="utf-8") as file:
            file.write(self.file_payload)
    