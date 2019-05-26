import numpy
import random
from Config import Config
from Loader import Loader
from items import *

class GeneticAlgorithm():

    # Create an initial seed population
    def seed(self):
        population = list()
        for individual in range(Config.population_size):
            population.append({'height': random.uniform(Config.min_height, Config.max_height), 'items': numpy.random.randint(0, item_count(), items_count())})
        return population

    def replacement(self, population):
        population_1 = Loader.replacement(1)(self, population)
        population_2 = Loader.replacement(2)(self, population)

        size_1 = int(Config.B * len(population_1))
        size_2 = int((1 - Config.B) * len(population_1))

        sample_1 = random.sample(population_1, size_1)
        sample_2 = random.sample(population_2, size_2)

        return numpy.append(sample_1, sample_2)

    def fitness(self, population):
    # Calculating the fitness value of each solution in the current population.   
        fitness_vector = list()
        for individual in population:
            arms = item_value(individual['items'][0], 0)
            boots = item_value(individual['items'][1], 1)
            helmets = item_value(individual['items'][2], 2)
            gloves = item_value(individual['items'][3], 3)
            vests = item_value(individual['items'][4], 4)
                
            strength = arms['strength'][0] + boots['strength'][0] + helmets['strength'][0] + gloves['strength'][0] + vests['strength'][0]
            agility = arms['agility'][0] + boots['agility'][0] + helmets['agility'][0] + gloves['agility'][0] + vests['agility'][0]
            skill = arms['skill'][0] + boots['skill'][0] + helmets['skill'][0] + gloves['skill'][0] + vests['skill'][0]
            resistence = arms['resistence'][0] + boots['resistence'][0] + helmets['resistence'][0] + gloves['resistence'][0] + vests['resistence'][0]
            life = arms['life'][0] + boots['life'][0] + helmets['life'][0] + gloves['life'][0] + vests['life'][0]

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

    def select_mating_pool(self, population, fitness, GA):
        population_1 = Loader.select(1)(population, fitness, GA)
        population_2 = Loader.select(2)(population, fitness, GA)

        size_1 = int(Config.A * len(population_1))
        size_2 = int((1 - Config.A) * len(population_1))

        sample_1 = random.sample(population_1, size_1)
        sample_2 = random.sample(population_2, size_2)

        return numpy.append(sample_1, sample_2)

    def crossover(self, parent1, parent2):
        return Loader.crossover()(parent1, parent2)

    def mutation(self, offspring):
        # TODO revisar que cambia random
        if (Config.mutation_uniformity == 2):
            Config.mutation_prob = random.uniform(0, 1)
        return Loader.mutation()(offspring)

