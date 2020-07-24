import os
from flora_fauna import RiverDolphin
from flora_fauna import GoldDustDayGecko
from flora_fauna import NeneGoose
from flora_fauna import Kikakapu
from flora_fauna import Pueo
from flora_fauna import Ulae
from flora_fauna import Opeapea
from flora_fauna import HappyFaceSpider

def release_animal(arboretum):
    available_animals = ["River Dolphin", "Gold Dust Day Gecko", "Nene Goose", "Kīkākapu", "Pueo", "'Ulae", "Ope'ape'a", "Happy-Face Spider"]

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, animal in enumerate(available_animals):
        print(f'{index + 1}. {animal}')

    print('\nChoose animal.')
    choice = input("> ")
    choosing_which_animal(arboretum, choice)


def choosing_which_animal(arboretum, choice):
    if choice == "1":
        animal = RiverDolphin()
        habitats = ['River', 'Coastline']
        biome1 = arboretum.habitats["rivers"] + arboretum.habitats["coastlines"]
    elif choice == "2":
        animal = GoldDustDayGecko()
        habitats = ['Forest']
        biome1 = arboretum.habitats["forests"]
    elif choice == "3":
        animal = NeneGoose()
        habitats = ['Grassland']
        biome1 = arboretum.habitats["grasslands"]
    elif choice == "4":
        animal = Kikakapu()
        habitats = ['Swamp', 'River']
        biome1 = arboretum.habitats["swamps"] + arboretum.habitats["rivers"]
    elif choice == "5":
        animal = Pueo()
        habitats = ['Grassland', 'Forest']
        biome1 = arboretum.habitats["grasslands"] + arboretum.habitats["forests"]
    elif choice == "6":
        animal = Ulae()
        habitats = ['Coastline']
        biome1 = arboretum.habitats["coastlines"]
    elif choice == "7":
        animal = Opeapea()
        habitats = ['Forest', 'Mountain']
        biome1 = arboretum.habitats["forests"] + arboretum.habitats["mountains"]
    elif choice == "8":
        animal = HappyFaceSpider()
        habitats = ['Swamp']
        biome1 = arboretum.habitats["swamps"]
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
        
    finding_which_biome(biome1, choice, animal, arboretum, habitats)


def finding_which_biome(biome1, choice, animal, arboretum, habitats):
    os.system('cls' if os.name == 'nt' else 'clear')
    checking_for_habitats = 0
    checking_for_max_population = 0
    for index, value in enumerate(biome1):
        if len(value.animal_population) < value.capacity_animal:
            checking_for_habitats += 1
            print(f'{index + 1}. {value.name} [{value.id}] ({len(value.animal_population)} animals)')
        elif len(value.animal_poplation) == value.capacity_animal:
            checking_max_population += value.name

    if checking_for_habitats == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        if checking_for_mac_population != 0:
            print(f'The ')
        elif len(habitats) > 1:
            print(f'No biomes available. Please create a {habitats[0]} biome or a {habitats[1]} biome for the {animal.species}')
        else:
            print(f'No biomes available. Please create a {habitats[0]} for the {animal.species}')
        input("\n\nPress any key to continue...")
        return
                    
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    try:
        animal_habitat = biome1[int(choice) - 1].name.lower() + 's'
        for index, val in enumerate(arboretum.habitats[animal_habitat]):
            if biome1[int(choice) - 1].id == val.id:
                arboretum.habitats[animal_habitat][index].addAnimal(animal)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice was not a valid input.')
        input("\n\nPress any key to continue...")
        return
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice is not in the range of choices.')
        input("\n\nPress any key to continue...")
        return
        