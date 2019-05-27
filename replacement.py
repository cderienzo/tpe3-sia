import random
from Config import Config

def one(GA, population, fitness):
    offspring = []

    while(len(population)!=0):
        parents = random.sample(population, 2)
        offspring.extend(GA.crossover(parents[0], parents[1]))
        population.remove(parents[0])
        population.remove(parents[1])
    
    offspring = GA.mutation(offspring)
    return offspring

def two(GA, population, fitness):
    # TODO buscar mejor manera sin hacer backup
    population_backup = population.copy
    parents = GA.select_mating_pool(population, fitness, 'A', GA,Config.num_parents_mating)

    offspring = []

    # TODO restarselo a pop asi no se repite
    while(len(parents)!=0):
        parents = random.sample(parents, 2)
        offspring.extend(GA.crossover(parents[0], parents[1]))
        population.remove(parents[0])
        population.remove(parents[1])

    offspring = GA.mutation(offspring)

    offspring.extend(GA.select_mating_pool(population_backup, fitness, 'B', GA, len(population_backup)-Config.num_parents_mating))
    return offspring    

def three(GA, population, fitness):
    # TODO buscar mejor manera sin hacer backup
    population_backup = population.copy
    parents = GA.select_mating_pool(population, fitness, 'A', GA, Config.num_parents_mating)

    offspring = []

    while(len(parents!=0)):
        parents = random.sample(parents, 2)
        offspring.extend(GA.crossover(parents[0], parents[1]))
        population.remove(parents[0])
        population.remove(parents[1])

    offspring = GA.mutation(offspring)

    new_pop = GA.select_mating_pool(population_backup, fitness, 'B', GA, len(population_backup)-Config.num_parents_mating)
    population_backup.extend(offspring)
    new_pop.extend(GA.select_mating_pool(population_backup, fitness, 'B', GA, Config.num_parents_mating))
    return new_pop