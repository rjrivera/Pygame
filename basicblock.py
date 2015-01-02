from Vec2d import Vec2d

class basicblock(object):
    """parent class, supports level construction as basic unit,
       and provides head of class hiearchy. 
       """
    __slots__ = ['x', 'y', 'width', 'height']    

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
