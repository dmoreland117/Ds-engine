from .scene import Scene
from .context import Context


class SceneManager:
    scenes:dict = {}
    current_scene_id:int = 0
    
    def __init__(self, context):
        self.context = context
    
    def add_scene(self, scene:Scene, name:str | None = None):
        scene.set_id(self.current_scene_id)
        if name:
            scene.set_name(name)    
                
        self.scenes[self.current_scene_id] = scene
        self.current_scene_id += 1
        scene.init()
    
    def remove_scene(self, id:int):
        return self.scenes.pop(id)
    
    def get_scene(self, id:int):
        return self.scenes.get(id, None)
    
    def get_scenes(self):
        for scene in self.scenes.values():
            print(scene.get_name())

    def update(self, dt):
        for scene in self.scenes:
            self.scenes[scene].update(dt)
    
    def input(self, dt):
        for scene in self.scenes:
            self.scenes[scene].input(dt)
    
    def render(self):
        for scene in self.scenes:
            self.scenes[scene].render()