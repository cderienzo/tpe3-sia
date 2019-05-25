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
        
        strength = 100*numpy.tanh(0.01*strength)
        agility = numpy.tanh(0.01*agility)
        skill = 0.6*numpy.tanh(0.01*skill)
        resistence = numpy.tanh(0.01*resistence)
        life = 100*numpy.tanh(0.01*life)

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
