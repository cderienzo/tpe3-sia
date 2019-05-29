import numpy
import random
from Config import Config
from Loader import Loader
from items import *
from State import State
class GeneticAlgorithm():

    # Create an initial seed population
    def seed(self):
        population = list()
        for individual in range(Config.N):
            population.append({'height': random.uniform(Config.min_height, Config.max_height), 'items': list(numpy.random.randint(0, item_count(), items_count()))})
        return population

    def replacement(self, population, fitness):
        return Loader.replacement()(self, population, fitness)

    def fitness(self, population):
    # Calculating the fitness value of each solution in the current population.   
        fitness_vector = list()
        for individual in population:
            arms = item_value(individual['items'][0], 0)
            boots = item_value(individual['items'][1], 1)
            helmets = item_value(individual['items'][2], 2)
            gloves = item_value(individual['items'][3], 3)
            vests = item_value(individual['items'][4], 4)
                
            strength = arms['Fu'] + boots['Fu'] + helmets['Fu'] + gloves['Fu'] + vests['Fu']
            agility = arms['Ag'] + boots['Ag'] + helmets['Ag'] + gloves['Ag'] + vests['Ag']
            skill = arms['Ex'] + boots['Ex'] + helmets['Ex'] + gloves['Ex'] + vests['Ex']
            resistence = arms['Re'] + boots['Re'] + helmets['Re'] + gloves['Re'] + vests['Re']
            life = arms['Vi'] + boots['Vi'] + helmets['Vi'] + gloves['Vi'] + vests['Vi']

            strength = 100 * numpy.tanh(0.01 * Loader.strength_multiplier * strength)
            agility = numpy.tanh(0.01 * Loader.agility_multiplier * agility)
            skill = 0.6 * numpy.tanh(0.01 * Loader.skill_multiplier * skill)
            resistence = numpy.tanh(0.01 * Loader.resistence_multiplier * resistence)
            life = 100 * numpy.tanh(0.01 * life)

            atm = 0.5 - pow((3 * individual['height'] - 5), 4) + pow((3 * individual['height'] - 5), 2) + individual['height']/2
            dem = 2 + pow((3 * individual['height'] - 5), 4)- pow((3 * individual['height'] - 5), 2) - individual['height']/2

            attack = (agility + skill) * strength * atm
            defense = (resistence + skill) * life * dem
            fitness = Loader.attack_multiplier * attack + Loader.defense_multiplier * defense
            fitness_vector.append(fitness)
        return fitness_vector

    def select_pool(self, population, fitness, selection_pair, GA, size):
        first, second = 3, 4
        factor = Config.B
        
        if(selection_pair == 'A'):
            first, second = 1, 2
            factor = Config.A 
    
        size_1 = int(factor * size)
        size_2 = size - size_1

        population_1 = Loader.select(first)(population, fitness, GA, size_1)
        population_2 = Loader.select(second)(population, fitness, GA, size_2)

        population_1.extend(population_2)
        return population_1

    def crossover(self, parent1, parent2):
        return Loader.crossover()(parent1, parent2)

    def mutation(self, offspring):
        if (Config.mutation_uniformity == 2):
            Config.p_m = Config.initial_p_m / (1 + Config.p_m_cooling_alpha * pow(State.generation,2))
        return Loader.mutation()(offspring)

