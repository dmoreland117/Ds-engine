from engine import Scene, pg, Text, Button

class TileModeMenu(Scene):
    modes = [
        '4bpp', '8bpp'
    ]
    mode_texts = []
    header_rect:pg.Rect = pg.Rect(0, 0, 640, 32)
    
    def __init__(self, context):
        super().__init__(context)
    
    def _initailized(self):
        txt = Text(self.context)
        txt.set_font_color((0,0,0))
        txt.set_text('Select Tile Mode')
        txt.set_position(8, 8)
        
        btn = Button(self.context)
        btn.set_position(640 - btn.width, 0)
        self.add_scene(txt, 'hdr_text')
        self.add_scene(btn, 'btn')
        
        ypos = 48
        for mode in self.modes:
            txt = Text(self.context)
            txt.set_font_color((255,255,255))
            txt.set_text(mode)
            txt.set_position(10, ypos)
            self.add_scene(txt, f"txt{mode}")
            ypos += 32

    def _render(self, renderer):
        self.draw_header(renderer)
        
    def draw_header(self, renderer):
        pg.draw.rect(renderer.get_screen(), (255, 255, 255), self.header_rect)
    