from engine import App, pg, Text, DColor
from tile_mode_menu import TileModeMenu

class Editor(App):
    def __init__(self, title, width, height, options = None):
        super().__init__(title, width, height, options)
       
        bg:DColor = (45, 45, 45)
       
        self.context.renderer.set_clear_color(bg)
       
        self.context.scenes.add_scene(TileModeMenu(self.context), 'tile_modes')
        print(self.context.scenes.get_scenes())


if __name__ == '__main__':
    editor = Editor("test", 640, 480)
    editor.run()