import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config
from State import State

def finished():
    finish = False
    if (Config.kicking):
        return kicking_finished()
    if (Config.max_generations):
        finish = finish or max_generations_finished()
    if not finish and (Config.structure):
        finish = finish or structure_finished()
    if not finish and (Config.content):
        finish = finish or content_finished()
    if not finish and (Config.near_optimal):
        finish = finish or near_optimal_finished()
    return finish        

def max_generations_finished():
    return State.generation >= Config.num_generations

def structure_finished():
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    fitness_changed = GA.fitness(changed)
    best_match_idx_changed = numpy.where(fitness_changed == numpy.max(fitness_changed))
    index_changed = best_match_idx_changed[0][0]
    if ((fitness_changed[index_changed] - fitness[index]) < Config.delta_variation_fitness):
        return False    

    return True

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
    return (Config.optimal_fitness - fitness[index]) < Config.delta 

def kicking_finished():
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    distance = Config.optimal_fitness - fitness[index]
    if  distance > Config.delta:         
        Config.p_m += Config.p_m*0.5*numpy.tanh(distance)
        return False

    return True

GA = GeneticAlgorithm()

population = GA.seed()

while(not finished()):
    fitness = GA.fitness(population)
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    print("gen: ", State.generation,"  fitness: ", fitness[index],"  height: ", population[index]['height'],"  items: ", population[index]['items'])

    population = GA.replacement(population, fitness)
    State.generation += 1

print("-------------------------------------------------------------------------")
print("Generation : ", State.generation)
print("-------------------------------------------------------------------------")
fitness = GA.fitness(population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]
print("best solution : ", population[index])
print("best solution fitness : ", fitness[index])
print("-------------------------------------------------------------------------") 
