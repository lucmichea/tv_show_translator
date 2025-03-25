import os
import ffmpeg

from utils.FilePathManager import FilePathManager
from utils.FileType import FileType

class VideoCombiner(object):

    def __init__(self, filePathManager: FilePathManager):
        self.filePathManager = filePathManager
    
    def combine(self):
        if not os.path.exists(self.filePathManager.get_file_path(FileType.VIDEO)):
            raise Exception(f"Video file not found at {self.filePathManager.get_file_path(FileType.VIDEO)}")
        
        if not os.path.exists(self.filePathManager.get_file_path(FileType.AUDIO)):
            raise Exception(f"Audio file not found at {self.filePathManager.get_file_path(FileType.AUDIO)}")

        if not os.path.exists(self.filePathManager.get_file_path(FileType.CAPTION)):
            raise Exception(f"Subtitle file not found at {self.filePathManager.get_file_path(FileType.CAPTION)}")

        output_path = self.filePathManager.get_file_path(FileType.COMBINED)
        video_input = ffmpeg.input(self.filePathManager.get_file_path(FileType.VIDEO))
        audio_input = ffmpeg.input(self.filePathManager.get_file_path(FileType.AUDIO))
        caption_input = ffmpeg.input(self.filePathManager.get_file_path(FileType.CAPTION))
        output_ffmpeg = ffmpeg.output(
            video_input,
            audio_input,
            caption_input,
            output_path,
            vcodec="copy",
            acodec="copy",
            scodec="webvtt",
        )
        output_ffmpeg = ffmpeg.overwrite_output(output_ffmpeg)
        print(f"Running the equivalent of: {ffmpeg.compile(output_ffmpeg)}")
        ffmpeg.run(output_ffmpeg)
