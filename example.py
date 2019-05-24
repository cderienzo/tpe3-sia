import numpy
import genetic_algorithm
import item_reader
"""
The target is to maximize the performance:
    performance = 0.1*attack + 0.9*defense
"""

# Inputs of the equation.
equation_inputs = [4,-2,3.5,5,-11,-4.7]

# Number of the weights we are looking to optimize. Ids from tsv
num_weights = 5

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 8
num_parents_mating = 4

# Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.randint(low=0, high=9, size=pop_size) 

print(new_population)

num_generations = 5
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measing the fitness of each chromosome in the population.    
    fitness = genetic_algorithm.cal_pop_fitness(new_population)

    # Selecting the best parents in the population for mating.
    parents = genetic_algorithm.select_mating_pool(new_population, fitness, 
                                      num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = genetic_algorithm.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = genetic_algorithm.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    print("Best solution : ", new_population[index])



# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = genetic_algorithm.cal_pop_fitness(new_population)

# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

index = best_match_idx[0][0]

print("Best solution : ", new_population[index])

print("Best solution fitness : ", fitness[index])
