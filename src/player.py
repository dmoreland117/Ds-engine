from engine import Sprite, Positioned

class Player(Positioned):
    new_pos_x:int = 0
    new_pos_y:int = 0
    def __init__(self, context):
        super().__init__(context)
        
    def _initailized(self):
        loaded = self.get_context().recources.load_recource('src/assets/Heimlich.png')
        if loaded:
            self.texture = self.get_context().recources.get_recource_by_id(0)
        
            self.sprite = Sprite(self.context)
            self.sprite.set_texture(self.texture)
            
            self.add_scene(self.sprite, 'player_sprite')
            
    def _input(self, input, dt):
        if input.action_pressed('up'):
            self.new_pos_y -= 1
        if input.action_pressed('down'):
            self.new_pos_y += 1
        if input.action_pressed('left'):
            self.new_pos_x -= 1
        if input.action_pressed('right'):
            self.new_pos_x += 1
            
    
    def _update(self, dt):
        self.set_position(self.new_pos_x, self.new_pos_y)
    
    def _render(self, renderer):
        pass