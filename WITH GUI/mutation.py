import numpy
from Config import Config
from State import State
from items import *


def gene(offspring_crossover):
    for offspring in offspring_crossover:
        if(numpy.random.random_sample() < Config.p_m):
            random_value = numpy.random.randint(0, items_count()+1)
            if(random_value == items_count()):
                mutate_height(offspring)
            else:
                mutation_value = numpy.random.random_integers(0, item_count())
                offspring['items'][random_value] = mutation_value 
    return offspring_crossover


def multigene(offspring_crossover):
    for offspring in offspring_crossover:
        for i in range(0,len(offspring['items'])):
            if(numpy.random.random_sample() < Config.p_m):  
                mutation_value = numpy.random.random_integers(0, item_count())
                offspring['items'][i] = mutation_value
        if(numpy.random.random_sample() < Config.p_m):
            mutate_height(offspring)
    return offspring_crossover


def mutate_height(offspring):
    if(Config.specialized_height_mutation):
        offset = get_height_offset()
        if(numpy.random.randint(0, 2) == 1):
            offset = -offset
        offspring['height'] += offset
        if(offspring['height']> Config.max_height):
            offspring['height'] = Config.max_height
        if(offspring['height']< Config.min_height):
            offspring['height'] = Config.min_height

    else:
        offspring['height'] = numpy.random.uniform(Config.min_height, Config.max_height)


def get_height_offset():
    return 10**-(1+State.generation//100)
