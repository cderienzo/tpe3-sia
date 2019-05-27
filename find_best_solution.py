import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config

def finished():
    switcher = {
        1: max_generations_finished,
        2: structure_finished,
        3: content_finished,
        4: near_optimal_finished
    }
    return switcher.get(Config.finish_criteria)()

def max_generations_finished():
    return generation >= Config.num_generations

def structure_finished():
    # TODO
    return False

def content_finished():
    global best_fitness_current
    global consecutive_generations
    
    if generation == 0:
        return False
    if (fitness[index] > best_fitness_current):
        best_fitness_current = fitness[index]
        consecutive_generations = 0
        return False
    else:
        consecutive_generations += 1
        return consecutive_generations >= Config.max_consecutive_generations     

def near_optimal_finished():
    if generation == 0:
        return False
    return abs(Config.optimal_fitness - fitness[index]) < Config.delta 

GA = GeneticAlgorithm()

population = GA.seed()

generation = 0
best_fitness_current = -1
consecutive_generations = 0

while(not finished()):
    print("Generation : ", generation)
    print("-------------------------------------------------------------------------")
    fitness = GA.fitness(population)
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    print("best solution : ", population[index])
    print("best solution fitness : ", fitness[index])
    print("-------------------------------------------------------------------------") 

    population = GA.replacement(population)
    generation += 1