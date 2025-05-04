import pygame as pg

class InputManager:
    quit_requested:bool
    actions:dict
    # {
    #   "jump": {
    #       'key': pg.K_j,
    #       'pressed': False,
    #       'just_pressed': False
    #   }
    # }
    mouse_pos_rel:tuple[int, int]
    mouse_pos_screen:tuple[int, int]
    
    def __init__(self):
        self.actions = {}
        self.quit_requested = False
        self.mouse_pos_rel = (0, 0)
        self.mouse_pos_screen = (0, 0)

    def set_action(self, name:str, key:int) -> None:
        self.actions[name] = {
            'key': key,
            'pressed': False,
            'released': False,
            'just_pressed': False
        }

    def remove_action(self, name:str) -> None:
        if self.has_action(name):
            self.actions.pop(name)

    def get_action(self, name:str) -> int:
        if self.has_action(name):
            return {
                'name': name,
                'action': self.actions[name]
            }

    def get_actions(self) -> dict:
       return self.actions

    def has_action(self, name:str) -> bool:
        return name in self.actions

    def action_pressed(self, name:str) -> bool:
        if self.has_action(name):
            return self.actions[name]['pressed']
        
        return False

    def action_just_pressed(self, name:str) -> bool:
        if self.has_action(name):
            return self.actions[name]['just_pressed']
        
        return False

    def action_released(self, name:str) -> bool:
        if self.has_action(name):
            return self.actions[name]['released']
        
        return False

    def get_mouse_pos(self) -> tuple[int, int]:
        return self.mouse_pos_screen
    
    def get_mouse_motion(self) -> tuple[int, int]:
        return self.mouse_pos_rel

    def is_quit_requested(self):
        return self.quit_requested

    def update(self) -> None:     
        events = pg.event.get()

        self._reset_just_pressed_and_released()

        for event in events:
            if event.type == pg.QUIT:
                self.quit_requested = True
            if event.type == pg.KEYDOWN:
                for name, action in self.actions.items():
                    if action['key'] == event.key:
                        self.actions[name]['pressed'] = True
                        self.actions[name]['just_pressed'] = True
            if event.type == pg.KEYUP:
                for name, action in self.actions.items():
                    if action['key'] == event.key:
                        self.actions[name]['pressed'] = False
                        self.actions[name]['released'] = True
            if event.type == pg.MOUSEMOTION:
                self.mouse_pos_rel = event.rel
                self.mouse_pos_screen = event.pos

    def _reset_just_pressed_and_released(self) -> None:
        for name, action in self.actions.items():
            if self.actions[name]['just_pressed']:
                self.actions[name]['just_pressed'] = False
            if self.actions[name]['released']:
                self.actions[name]['released'] = False