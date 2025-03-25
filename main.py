import os
import argparse
from typing import Dict
from utils.FilePathManager import FilePathManager
from utils.FileType import FileType

from Downloader.YoutubeDownloader import YoutubeDownloader
from Downloader.VideoCombiner import VideoCombiner

from Models.Subtitle import Subtitle

from CaptionFileCreator.WEBVTTFileCreator import WEBVTTFileCreator
from CaptionFileCreator.CaptionFileCreator import CaptionFileCreator

LANGUAGE = 'en-US'

def helper_str() -> str:
    return """To use this program, please provide at least 3 arguments in total:
- tv_show: The TV show name (required) (--tv_show or -t)
- season: The season number (required) (--season or -s)
- episode: The episode number (required) (--episode or -e)
- directory: The directory in which you want to save your shows (--directory or -d)

The --extension argument is optional and defaults to "vtt".

If you need help formatting your input or have questions, run the program with --help."""

def extract_args() -> Dict[str,object]:
    parser = argparse.ArgumentParser(description=helper_str())
    parser.add_argument('-t', '--tv_show', type=str, required=True)
    parser.add_argument('-s', '--season', type=int, required=True)
    parser.add_argument('-e', '--episode', type=int, required=True)
    parser.add_argument('-d', '--directory', type=str, default=os.path.dirname(__file__))
    parser.add_argument('--extension', type=str, default="vtt")
    
    args = parser.parse_args()
    return {
        'tv_show': args.tv_show,
        'season': args.season,
        'episode': args.episode,
        'directory': args.directory,
        'extension': args.extension,
    }

def create_caption_file_creator(extension: str, 
                                tv_show: str, 
                                season: int, 
                                episode: int, 
                                filePathManager: FilePathManager) -> CaptionFileCreator:
    res = None
    if extension.lower() == "vtt":
        res = WEBVTTFileCreator(language=LANGUAGE, tv_show=tv_show, season=season, episode=episode, filePathManager=filePathManager)
        res.add_caption(Subtitle(126000, 127000, "this is a test 1"))
        res.add_caption(Subtitle(150000, 151000, "this is a test 2"))
        res.add_caption(Subtitle(218000, 220000, "this is a test 3"))
        res.add_caption(Subtitle(234000, 237000, "this is a test 4"))
        res.add_caption(Subtitle(336000, 338000, "this is a test 5"))
    return res

def main(retry: int = 0):
    if retry > 1:
        return

    args_from_input = extract_args()
    print(f"Running with args: {args_from_input}")

    tv_show = args_from_input.get('tv_show', "")
    season = args_from_input.get('season', "")
    episode = args_from_input.get('episode', "")
    directory = args_from_input.get('directory', os.path.dirname(__file__))
    extension = args_from_input.get('extension', "vtt")

    filePathManager = FilePathManager(tv_show, season, episode, extension, directory)
    
    if os.path.exists(filePathManager.get_file_path(FileType.CAPTION)):
        override = bool(input("Would you like to override the caption file(True/False): \n> "))
        if not override:
            return

    if os.path.exists(filePathManager.get_file_path(FileType.VIDEO)):
        captionFileCreator = create_caption_file_creator(extension, tv_show, season, episode,  filePathManager)
        captionFileCreator.create_caption_file()
        videoCombiner = VideoCombiner(filePathManager=filePathManager)
        videoCombiner.combine()
        return
    
    video_url = input("Please fill in the url to the video: \n> ")
    print(f"Downloading video: {video_url}")
    yd = YoutubeDownloader(video_url, filePathManager)
    yd.download()
    main(retry=retry+1)  # Retry on video not downloaded yet
    


if __name__ == '__main__':
    main()

# python main.py --tv_show DiRenjie --season 1 --episode 1
# https://www.youtube.com/watch?v=I-E7TrD_pQI


# Create a calculation crossword
