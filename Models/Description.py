from Caption import Caption
from Models.Cues.Size import Size
from Models.Cues.Line import Line
from Models.Cues.Alignment import Alignment, AlignmentEnum
from typing import override

class Description(Caption):
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
        line = Line(10)
        self.add_cue(alignment)
        self.add_cue(size)
        self.add_cue(line)
