from engine.options import Options
from .input_manager import InputManager
from .renderer import Renderer
from .context import Context
import pygame as pg 
from sys import exit

from .scene_manager import SceneManager

class App:
    title:str
    width:int
    height:int
    
    paused:bool = False
    running:bool = True
    
    options:Options
    context:Context

    clock:pg.time.Clock
    screen:pg.Surface
    
    def __init__(self, title:str, width:int, height:int, options:Options = None):
        if not options:
            self.options = Options.get_from_args()
        else:
            self.options = options
        
        self.title = title
        self.width = width
        self.height = height
        self.fill_color = (0, 0, 0)
    
        pg.init()
        pg.display.set_caption(title)
        self.screen = pg.display.set_mode((width, height))
        if self.options.full_screen:
            pg.display.set_mode(flags=pg.FULLSCREEN)
        
        self.clock = pg.time.Clock()
        
        self.context = Context()

        self.context.scenes = SceneManager(self.context)
        self.context.input = InputManager()
        self.context.renderer = Renderer(self.screen)
    
    def input(self, dt:float) -> None:
        self.context.input.update()
        self.context.scenes.input(dt)
        self._input(self.context.input, dt)
    
    def _input(self, input:InputManager, dt:float) -> None:
        pass
    
    def update(self, dt:float) -> None:
        self.context.scenes.update(dt)
        self._update(dt)
    
    def _update(self, dt:float)-> None:
        pass
    
    def render(self, renderer:Renderer) -> None:
        self.context.renderer.clear_screen()
        self.context.scenes.render()
        self._render(renderer)
        
    def _render(self, renderer:Renderer) -> None:
        pass
    
    def run(self) -> None:
        self.running = True
        while self.running:
            if self.context.input.is_quit_requested(): break
            dt = self.clock.tick(60) / 1000.0
            self.input(dt)
            if not self.paused:
                self.update(dt)
                self.render(self.context.renderer)
            
            pg.display.flip()
        
        pg.quit()
        exit(0)
