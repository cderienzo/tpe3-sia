import random
from Config import Config
import numpy

def one(GA, population, fitness):
    offspring = []

    while(len(population)!=0):
        r1 = numpy.random.randint(low=0, high=len(population)-1)
        r2 = numpy.random.randint(low=0, high=len(population)-1)
        offspring.extend(GA.crossover(population[r1], population[r2]))
        del population[r1]
        del population[r2-1]
    
    offspring = GA.mutation(offspring)
    return offspring

def two(GA, population, fitness):
    parents = GA.select_pool(population, fitness, 'A', GA,Config.k)

    offspring = []

    while(len(parents)!=0):
        r1 = numpy.random.randint(low=0, high=len(parents))
        parent1 = parents[r1]
        del parents[r1]
        r2 = numpy.random.randint(low=0, high=len(parents))
        offspring.extend(GA.crossover(parent1, parents[r2]))
        del parents[r2]
    offspring = GA.mutation(offspring)

    offspring.extend(GA.select_pool(population, fitness, 'B', GA, len(population)-Config.k))
    return offspring    

def three(GA, population, fitness):
    parents = GA.select_pool(population, fitness, 'A', GA, Config.k)

    offspring = []

    while(len(parents)!=0):
        r1 = numpy.random.randint(low=0, high=len(parents)-1)
        r2 = numpy.random.randint(low=0, high=len(parents)-1)
        offspring.extend(GA.crossover(parents[r1], parents[r2]))
        del parents[r1]
        del parents[r2-1]

    offspring = GA.mutation(offspring)
    new_pop = GA.select_pool(population, fitness, 'B', GA, len(population)-Config.k)

    population.extend(offspring)
    new_pop.extend(GA.select_pool(population, fitness, 'B', GA, Config.k))
    return new_pop