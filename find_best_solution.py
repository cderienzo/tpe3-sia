import numpy
from genetic_algorithm import GeneticAlgorithm
import Items
from Config import Config

GA = GeneticAlgorithm()

population = GA.seed()

for generation in range(Config.num_generations):
    print("Generation : %d" % generation)
    population = GA.replacement(population)


# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = GA.fitness(population)

# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

index = best_match_idx[0][0]

print("Best solution : ", population[index])

print("Best solution fitness : ", fitness[index])
