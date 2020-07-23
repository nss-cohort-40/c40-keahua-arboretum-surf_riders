from .animal import Animal
from .identifiable import Identifiable
from ..characteristics import Forest

class GoldDustDayGecko(Animal, Identifiable, Forest):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko", 2)
        Identifiable.__init__(self)
        Forest.__init__(self)
        self.__prey = { "Crickets", "Worms", "Mosquitos", "Maggots" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal.')
        else:
            print(f'The gecko rejects the {prey}')

    def __str__(self):
        return f'Gecko {self.id} is in the house.'