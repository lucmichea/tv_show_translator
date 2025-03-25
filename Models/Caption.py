from __future__ import annotations
from Models.Cues.Alignment import Alignment
from Models.Cues.Cue import Cue

class Caption(object):

    def __init__(self, 
                 start_time: float, 
                 end_time: float, 
                 text: str):
        self.start_time = start_time
        self.end_time = end_time
        self.text = text
        self.cues : list[Cue] = []

    def update_start_time(self, start_time):
        self.start_time = start_time

    def update_end_time(self, end_time):
        self.end_time = end_time
    
    def update_text(self, text):
        self.text = text

    @staticmethod
    def convert_time_to_str(time: float):
        milliseconds = int(time % 1000)
        seconds = int((time // 1000) % 60)
        minutes = int((time // 60000) % 60)
        hours = int(time // 3600000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}" 
    
    def add_cue(self, cue: Cue):
        self.cues.append(cue)

    def to_json(self):
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'text': self.text
        }
    
    def to_webvtt_text(self):
        return f"""
{self.convert_time_to_str(self.start_time)} --> {self.convert_time_to_str(self.end_time)} {" ".join([c.convert() for c in self.cues])}
{self.text}
"""
    
    # Add additional text conversion based on type of file you want to write to.
