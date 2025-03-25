import cv2
import numpy as np
from . import ImageExtractor, SubtitlesExtractor

from typing import List, Callable


class AllImageExtractors(object):

    def __init__(self, video_file_path: str, frame_processor: Callable[[np.ndarray], None]):
        self.video_path = video_file_path
        self.frame_processor = frame_processor
        self.extractors : List[ImageExtractor] = self.create_extractors()
        pass

    def extract_all_images(self) -> None:
        try:
            # Open the video file
            cap = cv2.VideoCapture(self.video_path)
            
            if not cap.isOpened():
                raise ValueError("Could not open video file")
                
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # here we need to do a couple of things to make it more efficient. 
            # 1. Use a sliding window of frames. Ideally we want to process one frame every 10 frames to make the code more efficient.
            # 2. Although, we want to be able to determine when was the beginning and end of a subtitle for resubbing afterwards.
            # 3. Note that subtitles are quite sparse and so a lot of frames will be processed quickly and moved on without any other frame / window manipulation.
            for frame_counter in range(1, total_frames + 1):
                ret, frame = cap.read()
                
                if not ret:
                    break
                    
                # Process the frame (e.g., store it)
                self.frame_processor(frame)
            
        except Exception as e:
            print(f"Error extracting images from video: {str(e)}")
            return []
        
    def create_extractors(self) -> List[ImageExtractor]:
        return [SubtitlesExtractor()]