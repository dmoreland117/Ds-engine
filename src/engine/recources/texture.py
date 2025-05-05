from ..core.recource import Recource
import pygame as pg

class Texture(Recource):
    surface:pg.Surface
    
    def __init__(self):
        super().__init__()
    
    def _get_file_types(self):
        return [
            'jpg', 'jpeg', 'png'
        ]
    
    def _load(self, path):
        texture = Texture()
        texture.surface = pg.image.load(path)
        
        return texture
        
    def get_surface(self) -> pg.Surface:
        return self.surface
    