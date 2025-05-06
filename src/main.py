from engine import App, pg, Text, DColor, Sprite
from player import Player

class Editor(App):
    def __init__(self, title, width, height, options = None):
        super().__init__(title, width, height, options)
       
        bg:DColor = (45, 45, 45) 
        self.context.renderer.set_clear_color(bg)
       
        self.context.input.set_action('up', pg.K_UP)
        self.context.input.set_action('down', pg.K_DOWN)
        self.context.input.set_action('left', pg.K_LEFT)
        self.context.input.set_action('right', pg.K_RIGHT)
        
        
        self.context.scenes.add_scene(Player(self.context), 'player')
        print(self.context.scenes.get_scenes())

if __name__ == '__main__':
    editor = Editor("test", 640, 480)
    editor.run()