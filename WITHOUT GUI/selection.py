import numpy
import random
from Config import Config
from State import State

def elite(population, fitness, GA, size):
    population = population.copy()
    population.sort(key=lambda val: GA.fitness([val]))
    return population[len(population) - size:]

def roulette(population, fitness, GA, size):
    accumulated_fitness = accum_fitness(fitness)
    parents = []
    roulette_values = numpy.random.uniform(low=0.0, high=1.0, size=size)
    
    for i in range(size):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > roulette_values[i] and accumulated_fitness[k-1] < roulette_values[i]:
                parents.append(population[k])
            elif k==0 and accumulated_fitness[k] > roulette_values[i]:
                parents.append(population[k])

    return parents

def universal(population, fitness, GA, size):
    r = numpy.random.uniform(low=0.0,high=1.0)
    r_j = []

    for j in range(1, size + 1):
        r_j.append((r+j-1)/size)

    accumulated_fitness = accum_fitness(fitness)

    selection = []

    for i in range(size):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > r_j[i] and accumulated_fitness[k-1] < r_j[i]:
                selection.append(population[k])
                break
            elif accumulated_fitness[k] > r_j[i]:
                selection.append(population[k])
                break

    return selection

def boltzmann(population, fitness, GA, size):
    boltzmann_fitness = []
    schedule_id = Config.cooling_schedule
    if schedule_id == 1:
        temp_i = 1 + Config.initial_temperature / (1 + Config.cooling_alpha * pow(State.generation,2))
    elif schedule_id == 2:
        temp_i = 1 + Config.initial_temperature / (1 + (Config.cooling_alpha*numpy.log(State.generation+1)))
    elif schedule_id == 3:
        temp_i = 1 + Config.initial_temperature / ( 1 + Config.cooling_alpha*State.generation)
    elif schedule_id == 4:
        temp_i = 1 + Config.final_temperature + (Config.initial_temperature - Config.final_temperature)*((Config.num_generations - State.generation)/Config.num_generations)
    else:
        temp_i = Config.initial_temperature - State.generation * (Config.initial_temperature - Config.final_temperature)/Config.num_generations
    nom = numpy.exp(numpy.divide(fitness,temp_i))
    den = numpy.sum(nom)/len(fitness)
    boltzmann_fitness = nom/den

    return roulette(population, boltzmann_fitness, GA, size)

def deterministic_tournaments(population, fitness, GA, size):
    selection = []
    for i in range(size):
        participants = numpy.random.randint(low=0, high=len(population), size=Config.tournament_participants)
        index = -1
        for p in range(Config.tournament_participants):
            if index == -1:
                index = participants[0]
            elif fitness[index] < fitness[(participants[p])]:
                index = participants[p]
        selection.append(population[index])

    return selection

def probabilistic_tournaments(population, fitness, GA, size):
    selection = []
    for i in range(size):
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

    return selection

def ranking(population, fitness, GA, size):
    population = population.copy()
    population.sort(key=lambda val: GA.fitness([val]))
    selection = []
    for i in range(0,size):
        n = len(population)
        dividend = n * (n + 1) / 2

        p = [x/dividend for x in range(1,n+1)]

        r = random.choices(numpy.arange(0, n), p)
        selection.append(population[r[0]])
        del population[r[0]]

    return selection

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