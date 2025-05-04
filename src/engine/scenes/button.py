import pygame as pg
from .ui import UI

class Button(UI):
    mouse_inside:bool = False
    width:int = 48
    height:int = 32
    rect:pg.Rect
    color:pg.Color = (210, 210, 210)
    
    def __init__(self, context):
        super().__init__(context)
        
        wrld_pos = self.get_world_pos()
        
        self.rect = pg.Rect(wrld_pos[0], wrld_pos[1], self.width, self.height)
    
    def _input(self, input, dt):
        mouse_pos = input.get_mouse_pos()
        
        if (mouse_pos[0] > self.get_world_pos()[0] and mouse_pos[0] < self.get_world_pos()[0] + self.width) and (mouse_pos[1] > self.get_world_pos()[1] and mouse_pos[1] < self.get_world_pos()[1] + self.height):
            self.mouse_inside = True
        else:
            self.mouse_inside = False
    
    def _update(self, dt):
        if self.mouse_inside:
            self.color = (245, 245, 245)
        else:
            self.color = (210, 210, 210)
        
        wrld_pos = self.get_world_pos()
        
        self.rect = pg.Rect(wrld_pos[0], wrld_pos[1], self.width, self.height)
        
        
    def _render(self, renderer):
        pg.draw.rect(renderer.get_screen(), self.color, self.rect)