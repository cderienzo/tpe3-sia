import numpy
import random
from Config import Config

def one(GA, population):
    offspring = []

    while(len(offspring)<len(population)):
        parents = random.sample(population, 2)
        offspring.extend(GA.crossover(parents[0], parents[1]))
    
    offspring = GA.mutation(offspring)
    return offspring

def two(GA, population):
    fitness = GA.fitness(population)
    parents = GA.select_mating_pool(population, fitness)

    offspring = []

    while(len(offspring)<len(parents)):
        random_parents = random.sample(parents, 2)
        offspring.extend(GA.crossover(random_parents[0], random_parents[1]))

    offspring = GA.mutation(offspring)

    offspring.extend(random.sample(population,len(population)-Config.num_parents_mating))
    return offspring    

def three(GA, population):
    fitness = GA.fitness(population)
    parents = GA.select_mating_pool(population, fitness)

    offspring = []

    while(len(offspring)<len(parents)):
        random_parents = random.sample(parents, 2)
        offspring.extend(GA.crossover(random_parents[0], random_parents[1]))

    offspring = GA.mutation(offspring)

    new_pop = random.sample(population,len(population)-Config.num_parents_mating)

    return new_pop.extend(random.sample(population.extend(offspring), Config.num_parents_mating))
