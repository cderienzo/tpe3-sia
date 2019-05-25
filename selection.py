import numpy

def roulette_select_mating_pool(pop, accumulated_fitness, k_num):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.zeros((k_num, pop.shape[1]),numpy.int8)
    roulette_values = numpy.random.uniform(low=0.0,high=1.0, size=k_num)
    i=0
    k=0
    p=0
    for i in range(k_num):
        for k in range(len(accumulated_fitness)):
            if k > 0 and accumulated_fitness[k] > roulette_values[i] and accumulated_fitness[k-1] < roulette_values[i]:
                parents[p] = pop[k]
                p+=1
                break
            elif accumulated_fitness[k] > roulette_values[i]:
                parents[p] = pop[k]
                p+=1
                break
    return parents