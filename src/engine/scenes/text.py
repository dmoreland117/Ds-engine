from .ui import UI
import pygame as pg

class Text(UI):
    text:str
    font:pg.Font
    surface:pg.Surface
    color:pg.Color
    font_size:int

    def __init__(self, context):
        super().__init__(context)

        self.text = ''
        self.font_size = 24
        self.font = pg.Font(None, self.font_size)
    
    def _render(self, renderer):
        self.surface = self.font.render(self.text, True, self.color)

        pos = self.get_world_pos()

        renderer.draw_surface(self.surface, (pos[0], pos[1]))

    def set_text(self, text:str) -> None:
        self.text = text
    
    def set_font_color(self, color:pg.Color) -> None:
        self.color = color
    
    def set_font_size(self, size:int) -> None:
        self.font_size = size