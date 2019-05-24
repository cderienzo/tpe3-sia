import numpy
import item_reader

def cal_pop_fitness(pop):
    # Calculating the fitness value of each solution in the current population.   
    fitness_vector = []
    row_index = 0
    for row in pop:
        arms = item_reader.items(pop[row_index][0], 1)
        boots = item_reader.items(pop[row_index][1], 2)
        helmets = item_reader.items(pop[row_index][2], 3)
        gloves = item_reader.items(pop[row_index][3], 4)
        vests = item_reader.items(pop[row_index][4], 5)
        strength = float(arms[0])+ float(boots[0])+ float(helmets[0]) + float(gloves[0]) + float(vests[0])
        agility = float(arms[1])+ float(boots[1])+ float(helmets[1]) + float(gloves[1]) + float(vests[1])
        skill = float(arms[2])+ float(boots[2])+ float(helmets[2]) + float(gloves[2]) + float(vests[2])
        resistence = float(arms[3])+ float(boots[3])+ float(helmets[3]) + float(gloves[3]) + float(vests[3])
        life = float(arms[4])+ float(boots[4])+ float(helmets[4]) + float(gloves[4]) + float(vests[4])
        atm = 0.5 - pow((3*2-5),4) + pow((3*2-5),2) + 2/2
        dem = 2 + pow((3*2-5),4)- pow((3*2-5),2) - 2/2
        attack = (agility * skill) * strength * atm
        defense = (resistence * skill) * life * dem
        fitness = 0.1*attack + 0.9*defense
        fitness_vector.append(fitness)
        row_index+=1
    return fitness_vector

def cal_accum_fitness(pop, fitness):
    accumulated_fitness = numpy.empty(len(fitness))
    sum_fitness = numpy.sum(fitness)
    relative_fitness = numpy.divide(fitness,sum_fitness)
    i = 0
    for i in range(len(fitness)):
        if i == 0:
            accumulated_fitness[i] = relative_fitness[i]
        else:
            accumulated_fitness[i] = accumulated_fitness[i-1] + relative_fitness[i]
    return accumulated_fitness

def roulette_select_mating_pool(pop, accumulated_fitness, k_num):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((k_num, pop.shape[1]))
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
    return parents

def one_point_crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
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

def two_point_crossover(parents, offspring_size):
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

def uniform_crossover(parents, offspring_size, prob):
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

def gene_mutation(offspring_crossover, mutation_prob):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # Perform mutation on individual if random number < mutation_probability
        if(numpy.random.random_sample() < mutation_prob):
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
    return offspring_crossover

def multigene_mutation(offspring_crossover, mutation_prob):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        for idy in range(offspring_crossover.shape[1]):
            # Perform mutation on individual if random number < mutation_probability
            if(numpy.random.random_sample() < mutation_prob):
                random_value = numpy.random.uniform(-1.0, 1.0, 1)
                offspring_crossover[idx, idy] = offspring_crossover[idx, idy] + random_value
    return offspring_crossover

def select_new_generation(offspring, parents, pop_size):
    new_generation = parents.copy()
    return select_new_generation 