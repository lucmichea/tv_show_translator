import numpy as np
from typing import List
from . import Extractor

class SubtitlesExtractor(Extractor):

    def __init__(self): 
        # Adjust dimensions based on tv_show
        self.subtitles_upper_bound = 0.3
        self.subtitles_lower_bound = 0.1

    def extract(self, frame) -> List[np.ndarray]:
        extracted_frames = []
        extracted_frames.append(self.extract_subtitles(frame))
        extracted_frames.append(self.extract_all_but_subtitles(frame))
        return extracted_frames
    
    def extract_subtitles(self, frame):
        # Extract the subtitles portion of the frame
        height, _, _ = frame.shape
        start_row = max(0, height - int(height * self.subtitles_upper_bound))  
        end_row = max(0, height - int(height * self.subtitles_lower_bound))
        
        return frame[start_row:end_row] 

    def extract_all_but_subtitles(self, frame):
        # Extract the rest portion of the frame
        height, _, _ = frame.shape
        start_row = max(0, height - int(height * self.subtitles_upper_bound)) 

        return frame[:start_row]
    
# Example usage
if __name__ == '__main__':
    pass

# plan to test:
# 1. import a video
# 2. open the video and save three images (subtitles, location, parchment)
# 3. switch to jupyter notebook to increment faster (test grayscale etc for efficiency)
# 4. test the subtitles extractor, adjust the bounds accordingly
# 5. test the text extracted quickly to see if it works properly
# 6. take a look at frames too as we want to make sure it is 24 frames per seconds for accurate subs
