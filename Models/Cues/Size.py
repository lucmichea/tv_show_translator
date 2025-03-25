from typing import override

from Models.Cues.Cue import Cue

class Size(Cue):
    
    @override
    def __init__(self, size: int):
        self.size = size

    @override
    def get(self) -> int:
        return self.size
    
    @override
    def convert(self) -> str:
        return f"size:{self.size}%"
    