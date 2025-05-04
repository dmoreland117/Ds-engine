import pygame as pg

class Renderer:
    clear_color:pg.Color = (0, 0, 200)
    
    def __init__(self, screen):
        self.screen = screen

    def get_screen(self) -> pg.Surface:
        return self.screen
    
    def set_clear_color(self, color:pg.Color):
        self.clear_color = color
    
    def clear_screen(self, color:pg.Color | None = None) -> None:
        self.screen.fill(color if color else self.clear_color)
    
    def draw_surface(self, src:pg.Surface, pos, dest:pg.Surface | None = None):
        if not dest:
            self.screen.blit(src, pos)
        else:
            dest.blit(src, pos)