from typing import override

from Models.Caption import Caption
from Models.Cues.Alignment import Alignment, AlignmentEnum
from Models.Cues.Line import Line
from Models.Cues.Size import Size

class Subtitle(Caption):
    @override
    def __init__(self, 
                 start_time: float, 
                 end_time: float, 
                 text: str):

        super().__init__(start_time, 
                         end_time, 
                         text)
        alignment = Alignment(AlignmentEnum.CENTER)
        size = Size(100)
        line = Line(85)
        self.add_cue(alignment)
        self.add_cue(size)
        self.add_cue(line)
        
if __name__ == '__main__':
    FRAME_DURATION_MS = 41.7
    subtitle = Subtitle(1265341*FRAME_DURATION_MS, 64685543*FRAME_DURATION_MS, 'Hello, world!')
    print(subtitle.to_webvtt_text())
