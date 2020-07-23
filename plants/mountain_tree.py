from .plant import Plant
from .sunlight import Partial
from .resistance import HighResistance

class MountainTree(Plant, Partial, HighResistance):

    def __init__(self):
        Plant.__init__(self, 'Mountain Apple Tree', 'year-round', 17)
        Partial.__init__(self)
        HighResistance.__init__(self)