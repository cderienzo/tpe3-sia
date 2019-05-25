import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config

GA = GeneticAlgorithm()

population = GA.seed()

for generation in range(Config.num_generations):
    print("Generation : %d" % generation)
    population = GA.replacement(population)

fitness = GA.fitness(population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]

print("Best solution : ", population[index])
print("Best solution fitness : ", fitness[index])
