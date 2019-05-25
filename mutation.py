import numpy
from Config import Config

def gene(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # Perform mutation on individual if random number < mutation_probability
        if(numpy.random.random_sample() < Config.mutation_prob):
            random_value = numpy.random.randint(0, offspring_crossover.shape[1])
            mutation_value = numpy.random.random_integers(0,9)
            offspring_crossover[idx][random_value] = mutation_value
    return offspring_crossover

def multigene(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        for idy in range(offspring_crossover.shape[1]):
            # Perform mutation on individual if random number < mutation_probability
            if(numpy.random.random_sample() < Config.mutation_prob):                
                mutation_value = numpy.random.random_integers(0,9)
                offspring_crossover[idx, idy] = mutation_value
    return offspring_crossover