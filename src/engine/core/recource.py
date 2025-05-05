
class Recource:
    id:int = 0
    name:str = ''
    path:str = ''
    
    def __init__(self):
        pass
    
    def get_file_types(self) -> list[str]:
        return self._get_file_types()
    
    def _get_file_types(self) -> list[str]:
        pass
    
    def supports_file_type(self, type:str) -> bool:
        return self._supports_file_type(type)
    
    def _supports_file_type(self, type:str) -> bool:
        for t in self.get_file_types():
            if t == type:
                return True
        
        return False
    
    def load(self, path:str) -> 'Recource':
        return self._load(path)
    
    def _load(self, path:str) -> 'Recource':
        pass
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name:str):
        self.name = name