from .recource import Recource
from ..recources.texture import Texture
import os

class RecourceManager:
    id_counter:int = 0
    loaded_recources:dict = {}
    recource_types:list[Recource] = [
        Texture()
    ]
    
    def __init__(self):
        pass
    
    def load_recource(self, path:str, name:str | None = None) -> bool:
        LAST_ITEM = -1
        
        for r in self.recource_types:
            if r.supports_file_type(path.split('.')[LAST_ITEM]):
                self.loaded_recources[self.id_counter] = r.load(path)
                recource = self.loaded_recources[self.id_counter]
                
                if recource:
                    recource.id = self.id_counter
                    recource.path = path
                    recource.name = os.path.basename(path).split('.')[0]
                    self.id_counter += 1
                    return True
                
                return False
        
        return False
    
    def get_recource_by_id(self, id:int) -> Recource | None:
        return self.loaded_recources.get(id, None)
    
    def get_recource_by_name(self, name:str) -> Recource | None:
        for i, r in enumerate(self.loaded_recources.items()):
            if r.get_name() == name:
                return r
        
        return None
    
    