from ..core.scene import Scene

class Positioned(Scene):
    local_pos:tuple[int, int]
    rel_pos:tuple[int, int]

    def __init__(self, context):
        super().__init__(context)

        self.local_pos = (0, 0)
        self.rel_pos = (0, 0)

    def _parent_changed(self, parent):
        if isinstance(parent, Positioned):
            self.rel_pos = (
                    self.parent.rel_pos[0] + self.local_pos[0],
                    self.parent.rel_pos[1] + self.local_pos[1]
                )

    def get_position(self):
        return self.local_pos
    
    def set_position(self, x:int, y:int):
        self.local_pos = (x,y)

        if self.has_parent() and isinstance(self.parent, Positioned):
            self.rel_pos = (
                self.parent.rel_pos[0] + self.local_pos[0],
                self.parent.rel_pos[1] + self.local_pos[1]
            )
        else:
            self.rel_pos = self.local_pos
        
        for child in self.children:
            if isinstance(child, Positioned):
                child.parent_moved()
    
    def get_world_pos(self):
        return self.rel_pos

    def parent_moved(self):
        self.rel_pos = (
                self.parent.rel_pos[0] + self.local_pos[0],
                self.parent.rel_pos[1] + self.local_pos[1]
            )
        self._parent_moved()
    
    def _parent_moved(self):
        pass