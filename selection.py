import numpy
from Config import Config

def elite(population, fitness):
    # TODO
    return None

def roulette(population, fitness):
    # TODO redo con nueva estructura
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    accumulated_fitness = accum_fitness(fitness)
    parents = numpy.zeros((Config.num_parents_mating, population.shape[1]),numpy.int8)
    roulette_values = numpy.random.uniform(low=0.0,high=1.0, size=Config.num_parents_mating)
    p=0
    for i in range(Config.num_parents_mating):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > roulette_values[i] and accumulated_fitness[k-1] < roulette_values[i]:
                parents[p] = population[k]
                p+=1
                break
            elif accumulated_fitness[k] > roulette_values[i]:
                parents[p] = population[k]
                p+=1
                break
    return parents

def universal(population, fitness):
    # TODO
    return None

def boltzmann(population, fitness):
    # TODO
    return None

def tournaments1(population, fitness):
    # TODO
    return None

def tournaments2(population, fitness):
    # TODO
    return None

def ranking(population, fitness):
    # TODO
    return None

def accum_fitness(fitness):
    accumulated_fitness = numpy.empty(len(fitness))
    sum_fitness = numpy.sum(fitness)
    relative_fitness = numpy.divide(fitness,sum_fitness)
    for i in range(len(fitness)):
        if i == 0:
            accumulated_fitness[i] = relative_fitness[i]
        else:
            accumulated_fitness[i] = accumulated_fitness[i-1] + relative_fitness[i]
    return accumulated_fitness    