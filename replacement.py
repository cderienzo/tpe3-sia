def one(GA, population):
    fitness = GA.fitness(population)
    parents = GA.select_mating_pool(population, fitness)

    offspring_crossover = GA.crossover(parents)

    return GA.mutation(offspring_crossover)  

def two(GA, population):
    fitness = GA.fitness(population)
    parents = GA.select_mating_pool(population, fitness)

    return None    

def three(GA, population):
    # TODO
    return None

    fitness = GA.fitness(population)
    parents = GA.select_mating_pool(population, fitness)

    offspring_crossover = GA.crossover(parents)
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