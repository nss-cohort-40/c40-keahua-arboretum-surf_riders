from animals import Animal
from animals import Identifiable
from animals.characteristics import Saltwater
from animals.movements import Swimming

class Ulae(Animal, Saltwater, Swimming, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Ulae", age)
        Saltwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Flounder", "Mino", "Goober Fish" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Ulae ate the incredibly tasty {prey}')
        else:
            print(f'The Ulae spat out the {prey}')

    
    def __str__(self):
        return f'Ulae {self.id}. Razzzzzzzzzzor sharp teeth.'