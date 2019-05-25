import numpy
from Config import Config
import Loader

def one_point(parents):
    offspring_size = (2 * Config.num_parents_mating, Loader.item_count())
    offspring = numpy.zeros(offspring_size,numpy.int8)
    # The point at which crossover takes place between two parents. 
    crossover_point = numpy.random.randint(low=0, high=offspring_size[1])
    i = 0
    for k in range(parents.shape[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[i, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[i+1, 0:crossover_point] = parents[parent2_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[i, crossover_point:] = parents[parent2_idx, crossover_point:]
        offspring[i+1, crossover_point:] = parents[parent1_idx, crossover_point:]
        i+=2
    return offspring

def two_points(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The points at which crossover takes place between two parents. 
    crossover_point_1 = numpy.random.randint(low=0, high=offspring_size[1])
    crossover_point_2 = numpy.random.randint(low=crossover_point_1, high=offspring_size[1])
    i = 0
    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have from start to first crosspoint taken from the first parent.
        offspring[i, 0:crossover_point_1] = parents[parent1_idx, 0:crossover_point_1]
        offspring[i+1, 0:crossover_point_1] = parents[parent2_idx, 0:crossover_point_1]
        # The new offspring will have from first crosspoint to second crosspoint taken from the second parent.
        offspring[i, crossover_point_1:crossover_point_2] = parents[parent2_idx, crossover_point_1:crossover_point_2]
        offspring[i+1, crossover_point_1:crossover_point_2] = parents[parent1_idx, crossover_point_1:crossover_point_2]
        # The new offspring will have from second crosspoint to the end taken from the first parent.
        offspring[k, crossover_point_2:] = parents[parent1_idx, crossover_point_2:]
        offspring[k, crossover_point_2:] = parents[parent2_idx, crossover_point_2:]
    return offspring

def uniform(parents, offspring_size, prob):
    offspring = numpy.empty(offspring_size)

    for k in range(offspring_size[0]):
        for b in range(offspring_size[1]):             
            # Index of the first parent to mate.
            parent1_idx = k%parents.shape[0]
            # Index of the second parent to mate.
            parent2_idx = (k+1)%parents.shape[0]

            offspring[k] = parents[parent1_idx].copy()
            offspring[k+1] = parents[parent2_idx].copy()

            if(numpy.random.random_sample()<prob):
                offspring[k][b],  offspring[k+1][b] = offspring[k+1][b], offspring[k][b]
    return offspring

def anular(parents):
    # TODO
    return None    