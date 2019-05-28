import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config
from State import State

def finished():
    switcher = {
        1: max_generations_finished,
        2: structure_finished,
        3: content_finished,
        4: near_optimal_finished
    }
    return switcher.get(Config.finish_criteria)()

def max_generations_finished():
    return State.generation >= Config.num_generations

def structure_finished():
    # TODO
    return False

def content_finished():

    if State.generation == 0:
        return False
    if (fitness[index] > State.best_fitness_current):
        State.best_fitness_current = fitness[index]
        State.consecutive_generations = 0
        return False
    else:
        State.consecutive_generations += 1
        return State.consecutive_generations >= Config.max_consecutive_generations     

def near_optimal_finished():
    if State.generation == 0:
        return False
    return abs(Config.optimal_fitness - fitness[index]) < Config.delta 

GA = GeneticAlgorithm()

population = GA.seed()

while(not finished()):
    print("Generation : ", State.generation)
    print("-------------------------------------------------------------------------")
    fitness = GA.fitness(population)
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    print("best solution : ", population[index])
    print("best solution fitness : ", fitness[index])
    print("-------------------------------------------------------------------------") 

    population = GA.replacement(population, fitness)
    State.generation += 1

print("Generation : ", State.generation)
print("-------------------------------------------------------------------------")
fitness = GA.fitness(population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]
print("best solution : ", population[index])
print("best solution fitness : ", fitness[index])
print("-------------------------------------------------------------------------") 
