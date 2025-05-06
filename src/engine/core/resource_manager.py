from .resource import Resource
from ..resources.texture import Texture
import os

class ResourceManager:
    id_counter:int = 0
    loaded_resources:dict = {}
    resource_types:list[Resource] = [
        Texture()
    ]
    
    def __init__(self):
        pass
    
    def load_resource(self, path:str, name:str | None = None) -> bool:
        LAST_ITEM = -1
        
        for r in self.resource_types:
            if r.supports_file_type(path.split('.')[LAST_ITEM]):
                self.loaded_resources[self.id_counter] = r.load(path)
                resource = self.loaded_resources[self.id_counter]
                
                if resource:
                    resource.id = self.id_counter
                    resource.path = path
                    # if no custom name set to the file name
                    resource.name = name if not name else os.path.basename(path).split('.')[0]
                    self.id_counter += 1
                    return True
                
                return False
        
        return False
    
    def unload_resource(self, id:int):
        self.loaded_resources[id].unload()
        self.loaded_resources.pop(id)
    
    def get_resource_by_id(self, id:int) -> Resource | None:
        return self.loaded_resources.get(id, None)
    
    def get_resource_by_name(self, name:str) -> Resource | None:
        for i, r in enumerate(self.loaded_resources.items()):
            if r.get_name() == name:
                return r
        
        return None
    
    def get_resources(self) -> dict:
        return self.loaded_resources
    
    