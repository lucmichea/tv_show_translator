from enum import Enum
from typing import override

from Models.Cues.Cue import Cue

class AlignmentEnum(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Alignment(Cue):
    @override
    def __init__(self, alignment: AlignmentEnum):
        self.alignment = alignment

    @override
    def get(self) -> AlignmentEnum:
        return self.alignment
    
    @override
    def convert(self) -> str:
        return f"align:{self.alignment.value}"
    