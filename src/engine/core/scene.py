from .context import Context
from .input_manager import InputManager
from .renderer import Renderer
#add a collision scene and set up its rect

class Scene:
    id:int
    index:int
    paused:bool
    context:Context
    name:str = ''
    
    parent:'Scene' 
    children:list

    visible:bool = True
    
    def __init__(self, context:Context):
        self.context = context
        self.children = []
        self.parent = None

    def init(self):
        self._initailized()

    def _initailized(self):
            pass

    def update(self, dt:float):
        self._update(dt)
    
    def _update(self, dt:float):
        pass
    
    def input(self, dt:float):
        self._input(self.context.input, dt)
    
    def _input(self, input:InputManager, dt:float):
        pass
    
    def render(self):
        if self.visible:
            self._render(self.context.renderer)
    
    def _render(self, renderer:Renderer):
        pass
    
    def _parent_changed(self, parent:'Scene'):
        pass

    def get_context(self) -> Context:
        return self.context
    
    def set_parent(self, scene:'Scene') -> None:
        self.parent = scene
        self._parent_changed(scene)

    def has_parent(self):
        if self.parent:
            return True
        else: 
            return False

    def get_scene(self, path:str) -> 'Scene':
        return self.context.scenes.get_scene(path)

    def add_scene(self,scene:'Scene', name:str | None = None) -> None:
        self.children.append(scene)
        scene.set_parent(self)
        self.get_context().scenes.add_scene(scene, name)

    def set_name(self, name:str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_id(self, id:int):
        self.id = id

    def set_index(self, i:int):
        self.index = i

    def set_visibility(self, show:bool):
        if show == None:
            self.visible = not self.visible
            return self.visible
        
        self.visible = show