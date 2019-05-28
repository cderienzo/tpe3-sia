import numpy
import random
from Config import Config
from find_best_solution import generation

def elite(population, fitness, GA, size):
    population.sort(key=lambda val: GA.fitness([val]))
    return random.sample(population[len(population) - Config.num_parents_mating:], size)

def roulette(population, fitness, GA, size):
    accumulated_fitness = accum_fitness(fitness)
    parents = []
    roulette_values = numpy.random.uniform(low=0.0,high=1.0, size=Config.num_parents_mating)
    
    for i in range(Config.num_parents_mating):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > roulette_values[i] and accumulated_fitness[k-1] < roulette_values[i]:
                parents.append(population[k])
            elif k==0 and accumulated_fitness[k] > roulette_values[i]:
                parents.append(population[k])

    return random.sample(parents, size)

def universal(population, fitness, GA, size):
    r = numpy.random.uniform(low=0.0,high=1.0)
    r_j = []

    for j in range(1, Config.num_parents_mating + 1):
        r_j.append((r+j-1)/Config.num_parents_mating)

    accumulated_fitness = accum_fitness(fitness)

    selection = []

    for i in range(Config.num_parents_mating):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > r_j[i] and accumulated_fitness[k-1] < r_j[i]:
                selection.append(population[k])
                break
            elif accumulated_fitness[k] > r_j[i]:
                selection.append(population[k])
                break

    return random.sample(selection, size)

def boltzmann(population, fitness, GA, size):
    global generation
    boltzmann_fitness = []
    temp_i = Config.initial_temperature - generation * (Config.initial_temperature - Config.final_temperature)/Config.num_generations
    for i in len(fitness):
        norm += numpy.exp(numpy.divide(fitness,Config.initial_temperature))
    norm = norm/len(fitness)
    for i in len(fitness):
        boltzmann_fitness.append(numpy.exp(numpy.divide(fitness,Config.initial_temperature))/norm)
    return roulette(population, boltzmann_fitness, GA, size)

def tournaments1(population, fitness, GA, size):
    selection = []
    for i in range(Config.tournament_rounds):
        participants = numpy.random.randint(low=0, high=len(population), size=Config.num_parents_mating)
        index = -1
        for p in range(Config.num_parents_mating):
            if index == -1:
                index = participants[0]
            elif fitness[index] < fitness[(participants[p])]:
                index = participants[p]
            selection.append(population[index])

    return random.sample(selection, size)

def tournaments2(population, fitness, GA, size):
    selection = []
    for i in range(Config.num_parents_mating):
        participants = numpy.random.randint(low=0, high = len(population), size= 2)
        if numpy.random.random_sample() < 0.75:
            if fitness[participants[0]] < fitness[participants[1]]:
                selection.append(population[participants[1]])
            else:
                selection.append(population[participants[0]])
        else:
            if fitness[participants[0]] < fitness[participants[1]]:
                selection.append(population[participants[0]])
            else:
                selection.append(population[participants[1]])

    return random.sample(selection, size)

def ranking(population, fitness, GA, size):
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