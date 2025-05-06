from ..core.resource import Resource
import pygame as pg

class Texture(Resource):
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
    
    def _unload(self):
        self.surface = None
        
    def get_surface(self) -> pg.Surface:
        return self.surface
    