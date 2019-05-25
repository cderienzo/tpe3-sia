import numpy
import random
from Items import Items
from Config import Config
from Loader import Loader

class GeneticAlgorithm():
    def __init__(self):
        self.items = Items(Config.files)
        self.items_count = len(Config.files)
        self.item_count = self.items.item_count()

    # Create an initial seed population
    def seed(self):
        population = list()
        for individual in range(Config.population_size):
            population.append({'height': random.uniform(Config.min_height, Config.max_height), 'items': numpy.random.randint(0, self.item_count, self.items_count)})
        return population

    def replacement(self, population):
        return Loader.replacement()(self, population)    

    def fitness(self, population):
    # Calculating the fitness value of each solution in the current population.   
        fitness_vector = list()
        for individual in population:
            arms = self.items.item_value(individual['items'][0], 0)
            boots = self.items.item_value(individual['items'][1], 1)
            helmets = self.items.item_value(individual['items'][2], 2)
            gloves = self.items.item_value(individual['items'][3], 3)
            vests = self.items.item_value(individual['items'][4], 4)
            strength = arms[0] + boots[0] + helmets[0] + gloves[0] + vests[0]
            agility = arms[1] + boots[1] + helmets[1] + gloves[1] + vests[1]
            skill = arms[2] + boots[2] + helmets[2] + gloves[2] + vests[2]
            resistence = arms[3] + boots[3] + helmets[3] + gloves[3] + vests[3]
            life = arms[4] + boots[4]+ helmets[4] + gloves[4] + vests[4]
            
            strength = 100 * numpy.tanh(0.01 * Loader.strength_multiplier * strength)
            agility = numpy.tanh(0.01 * Loader.agility_multiplier * agility)
            skill = 0.6 * numpy.tanh(0.01 * Loader.skill_multiplier * skill)
            resistence = numpy.tanh(0.01 * Loader.resistence_multiplier * resistence)
            life = 100 * numpy.tanh(0.01 * life)

            atm = 0.5 - pow((3 * individual['height'] - 5), 4) + pow((3 * individual['height'] - 5), 2) + individual['height']/2
            dem = 2 + pow((3 * individual['height'] - 5), 4)- pow((3 * individual['height'] - 5), 2) - individual['height']/2

            attack = (agility * skill) * strength * atm
            defense = (resistence * skill) * life * dem
            fitness = Loader.attack_multiplier * attack + Loader.defense_multiplier * defense
            fitness_vector.append(fitness)
        return fitness_vector

    def select_mating_pool(self, population, fitness):
        return Loader.select()(population, fitness)

    def crossover(self, parents):
        return Loader.crossover()(parents)

    def mutation(self, offspring):
        # TODO revisar que cambia random
        if (Config.mutation_uniformity == 2):
            Config.mutation_prob = random.uniform(0, 1)
        return Loader.mutation()(offspring)

