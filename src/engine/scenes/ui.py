from .positioned import Positioned
from enum import Enum

class Alignment(Enum):
    start = 0
    center = 1
    end = 2

class UI(Positioned):
    h_align = Alignment.center
    v_align = Alignment.center
    
    padding = 0
    margin = 0
    
    
    def __init__(self, context):
        super().__init__(context)