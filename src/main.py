from engine import App, pg, Text, DColor, Sprite
from tile_mode_menu import TileModeMenu

class Editor(App):
    def __init__(self, title, width, height, options = None):
        super().__init__(title, width, height, options)
       
        bg:DColor = (45, 45, 45)
       
        self.context.renderer.set_clear_color(bg)
       
        self.context.recources.load_recource('src/assets/Heimlich.png')
       
        texture = self.context.recources.get_recource_by_id(0)
       
        test_sprite = Sprite(self.context)
        test_sprite.set_texture(texture)
        test_sprite.set_position(50, 50)
       
        self.context.scenes.add_scene(TileModeMenu(self.context), 'tile_modes')
        self.context.scenes.add_scene(test_sprite, 'test_spr')
        print(self.context.scenes.get_scenes())


if __name__ == '__main__':
    editor = Editor("test", 640, 480)
    editor.run()