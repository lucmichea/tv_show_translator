from typing import override

from Models.Cues.Cue import Cue

class Position(Cue):

    @override
    def __init__(self, pos: int):
        self.pos = pos

    @override
    def get(self) -> int:
        return self.pos
    
    @override
    def convert(self) -> str:
        return f"position:{self.pos}%"
    