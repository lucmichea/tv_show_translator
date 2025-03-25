from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable, VideoRegionBlocked, VideoPrivate, MaxRetriesExceeded
import os
from utils.FilePathManager import FilePathManager
from utils.FileType import FileType


class YoutubeDownloader(object):
    DOWNLOAD_FOLDER = "_shows"

    def __init__(self, 
                 video_url: str, 
                 filePathManager: FilePathManager):
        self.video_url = video_url
        self.filePathManager = filePathManager
        
    def download(self):
        try: 
            ytVideoConn = YouTube(self.video_url, 
                                  on_progress_callback=on_progress) 
        except: 
            print("Connection Error")
            return

        ytVideo = ytVideoConn.streams.filter(adaptive=True, file_extension='mp4', res='1080p').first() # .order_by('resolution')
        ytAudio = ytVideoConn.streams.filter(only_audio=True).first()
        # typically progressive have audio embedded and adaptive no, but adaptive have way better quality...
        # https://stackoverflow.com/questions/58184585/how-to-combine-audio-and-video-in-pytube

        self.create_folders()
        try:
            videoPath = ytVideo.download(self.filePathManager.download_path)
            self.rename_file(videoPath, FileType.VIDEO)
            audioPath = ytAudio.download(self.filePathManager.download_path)
            self.rename_file(audioPath, FileType.AUDIO)
        except (VideoUnavailable, VideoRegionBlocked, VideoPrivate, MaxRetriesExceeded) as e:
            print("Download Error")
            return
        
    def create_folders(self):
        os.makedirs(self.filePathManager.get_download_path(), exist_ok=True)

    def rename_file(self, out_file: str, type: FileType):
        os.rename(out_file, self.filePathManager.get_file_path(type))
