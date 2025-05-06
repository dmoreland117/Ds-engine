from .positioned import Positioned
from ..resources.texture import Texture

class Sprite(Positioned):
    texture:Texture

    def __init__(self, context):
        super().__init__(context)
        
        self.texture = None
    
    def _render(self, renderer):
        if self.texture:
            renderer.draw_surface(self.texture.get_surface(), self.get_world_pos())
        
    def set_texture(self, texture:Texture):
        self.texture = texture