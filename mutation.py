import numpy
from Config import Config
from items import *

def gene(offspring_crossover):
    for offspring in offspring_crossover:
        if(numpy.random.random_sample() < Config.p_m):
            random_value = numpy.random.randint(0, items_count()+1)
            if(random_value == items_count()):
                mutation_value = numpy.random.uniform(Config.min_height, Config.max_height)
                offspring['height'] = mutation_value
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
            offspring['height'] = numpy.random.uniform(Config.min_height, Config.max_height)
    return offspring_crossover