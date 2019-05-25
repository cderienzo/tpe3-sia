def one(GA, population):
    # TODO
    return None

def two(GA, population):
    # TODO
    return None    

def three(GA, population):
    # TODO
    return None

def four(GA, population):
    # TODO
    return None


# Measuring the fitness of each chromosome in the population.    
fitness = GA.fitness(population)

parents = GA.select_mating_pool(population, fitness)

# Generating next generation.
offspring_crossover = GA.crossover(parents)

# Mutating some of the offspring.
offspring_mutation = GA.mutation(offspring_crossover)

# Select which ones make it to the new generation
total_pool = numpy.append(parents, offspring_mutation,axis=0)
fitness = GA.fitness(total_pool)
next_generation = GA.select_mating_pool(total_pool, fitness)
new_population = next_generation
# Creating the new population based on the parents and offspring.
#new_population[0:parents.shape[0], :] = parents
#new_population[parents.shape[0]:, :] = offspring_mutation

fitness = GA.fitness(new_population)
# The best result in the current iteration.
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]
print("Best solution : ", new_population[index])    