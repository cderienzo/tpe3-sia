import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config

GA = GeneticAlgorithm()

population = GA.seed()

print("--------------------------------------------------------------------------")
print("Generation :  0")
print("--------------------------------------------------------------------------")
fitness = GA.fitness(population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]
print("best solution : ", population[index])
print("best solution fitness : ", fitness[index])
print("-------------------------------------------------------------------------")
for generation in range(0,Config.num_generations):
    population = GA.replacement(population)
    print("Generation : ", generation+1)
    print("-------------------------------------------------------------------------")
    fitness = GA.fitness(population)
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    print("best solution : ", population[index])
    print("best solution fitness : ", fitness[index])
    print("-------------------------------------------------------------------------")
