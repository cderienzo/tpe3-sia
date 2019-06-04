import pandas
from Config import Config
from selection import *
from crossover import *
from mutation import *
from replacement import *

class Loader:

    characters = {'Guerrero': {'attack_multiplier': 0.6,
                               'defense_multiplier': 0.4,
                               'options': [[1.1, 0.9, 0.8, 1, 0.9],
                                           [1.2, 1, 0.8, 0.8, 0.8],
                                           [0.8, 0.9, 0.9, 1.2, 1,1],
                                           [1, 1.1, 1, 1, 1]]},
                  'Arquero': {'attack_multiplier': 0.9,
                              'defense_multiplier': 0.1,
                              'options': [[0.8, 1.1, 1.1, 0.9, 0.7],
                                          [0.9, 1.1, 1, 0.9, 0.8],
                                          [0.8, 0.8, 0.8, 1.1, 1.2]]},
                  'Defensor': {'attack_multiplier': 0.1,
                              'defense_multiplier': 0.9,
                              'options': [[1, 0.9, 0.7, 1.2, 1.1],
                                          [1.1, 0.8, 0.8, 1.1, 1.1],
                                          [0.9, 0.9, 0.9, 1, 1.3],
                                          [0.8, 0.9, 1.2, 1.2, 0.8]]},
                  'Asesino': {'attack_multiplier': 0.7,
                              'defense_multiplier': 0.3,
                              'options': [[0.8, 1.2, 1.1, 1, 0.8],
                                          [0.9, 1, 1.1, 1, 0.9],
                                          [0.9, 0.9, 1, 1.1, 1]]}}                        

    attack_multiplier = characters[Config.character]['attack_multiplier']
    defense_multiplier = characters[Config.character]['defense_multiplier']
    strength_multiplier = characters[Config.character]['options'][Config.character_num][0]
    agility_multiplier = characters[Config.character]['options'][Config.character_num][1]
    skill_multiplier = characters[Config.character]['options'][Config.character_num][2]
    resistence_multiplier = characters[Config.character]['options'][Config.character_num][3]
    life_multiplier = characters[Config.character]['options'][Config.character_num][4]

    def replacement():
        switcher = {
        1: one,
        2: two,
        3: three
        }    
        return switcher.get(Config.replacement_method)           
    
    def select(number):
        switcher = {
        1: elite,
        2: roulette,
        3: universal,
        4: boltzmann,
        5: deterministic_tournaments,
        6: probabilistic_tournaments,
        7: ranking
        }
        if (number == 1):
            return switcher.get(Config.selection_method_1)
        elif (number == 2):
            return switcher.get(Config.selection_method_2)
        elif (number == 3):
            return switcher.get(Config.selection_method_3)
        else:
            return switcher.get(Config.selection_method_4)

    def crossover():
        switcher = {
        1: one_point,
        2: two_points,
        3: uniform,
        4: anular
        }
        return switcher.get(Config.crossover)

    def mutation():
        switcher = {
        1: gene,
        2: multigene
        }
        return switcher.get(Config.mutation_geneticity) 
