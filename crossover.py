import numpy
from Config import Config
from Loader import Loader
from offspring import *

def one_point(parent1, parent2):
    offspring1 = create_offspring()
    offspring2 = create_offspring()

    crossover_point = numpy.random.randint(low=0, high=Loader.items_count())
    
    offspring1['height'] = parent1['height']
    offspring2['height'] = parent2['height']

    offspring1['items'][0:crossover_point] = parent1['items'][0:crossover_point]
    offspring2['items'][0:crossover_point] = parent2['items'][0:crossover_point]

    offspring1['items'][crossover_point:] = parent2['items'][crossover_point:]
    offspring2['items'][crossover_point:] = parent1['items'][crossover_point:]

    return [offspring1, offspring2]

def two_points(parent1, parent2):
    offspring1 = create_offspring()
    offspring2 = create_offspring()

    crossover_point_1 = numpy.random.randint(low=0, high=Loader.items_count())
    crossover_point_2 = numpy.random.randint(low=crossover_point_1, high=Loader.items_count())

    offspring1['height'] = parent1['height']
    offspring2['height'] = parent2['height']

    offspring1['items'][0:crossover_point_1] = parent1[0:crossover_point_1]
    offspring2['items'][0:crossover_point_1] = parent2[0:crossover_point_1]

    offspring1['items'][crossover_point_1:crossover_point_2] = parent2[crossover_point_1:crossover_point_2]
    offspring2['items'][crossover_point_1:crossover_point_2] = parent1[crossover_point_1:crossover_point_2]

    offspring1['items'][crossover_point_2:] = parent1[crossover_point_2:]
    offspring2['items'][crossover_point_2:] = parent2[crossover_point_2:]

    return [offspring1, offspring2]

def uniform(parent1, parent2):
    offspring1 = create_offspring()
    offspring2 = create_offspring()

    rand_height = numpy.random.rand()

    offspring1['height'] = parent1['height'] if rand_height >= Config.uniform_crossover_p else parent2['height']
    offspring2['height'] = parent2['height'] if rand_height >= Config.uniform_crossover_p else parent1['height']

    for i in range(0, Config.items_count):
        p = numpy.random.rand()
        
        offspring1['items'][i] = parent1['items'][i] if(p>=Config.uniform_crossover_p) else parent2['items'][i]
        offspring2['items'][i] = parent2['items'][i] if(p>=Config.uniform_crossover_p) else parent1['items'][i]
    return [offspring1, offspring2]

def anular(parents):
    # TODO
    return None    