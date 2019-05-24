import numpy
import item_reader

def cal_pop_fitness(pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function caulcuates the sum of products between each input and its corresponding weight.
    
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

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover