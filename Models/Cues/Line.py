from typing import override

from Models.Cues.Cue import Cue

class Line(Cue):

    @override
    def __init__(self, line: int):
        self.line = line

    @override
    def get(self) -> int:
        return self.line

    @override
    def convert(self) -> str:
        return f"line:{self.line}%"
