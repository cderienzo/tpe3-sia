import numpy
import sys
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config
from State import State
from gui.mainwindow import Ui_GeneticAlgorithm
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt 

changed = Config.N

class MainWindow(QMainWindow, Ui_GeneticAlgorithm):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        global changed
        self.pushButton.setEnabled(False)

        GA = GeneticAlgorithm()

        population = GA.seed()

        # use ggplot style for more sophisticated visuals 
        plt.style.use('ggplot') 
        changed_line = [] 
        fit_line = [] 
        changed_x_vec = [] 
        changed_y_vec = [] 
        fit_line_x_vec = [] 
        fit_line_y_vec = [] 

        fitness = None
        index = None

        first = QPixmap('gui/first.png')
        second = QPixmap('gui/second.png')
        third = QPixmap('gui/third.png')
        forth = QPixmap('gui/forth.png')
        fifth = QPixmap('gui/fifth.png')
        previmage = None
        image = first

        while(not finished(GA, population, fitness, index)):
            fitness = GA.fitness(population)
            best_match_idx = numpy.where(fitness == numpy.max(fitness))
            index = best_match_idx[0][0]
            
            if(Config.graph_fit==1): 
                fit_line_x_vec=numpy.append(fit_line_x_vec, State.generation) 
                fit_line_y_vec=numpy.append(fit_line_y_vec, fitness[index]) 
                fit_line = live_plotter(fit_line_x_vec,fit_line_y_vec,fit_line,"Generations","Fitness","Fitness per generation") 
  
            if(Config.graph_std==1):
                changed_y = changed 
                if (type(changed) != int):
                    changed_y = len(changed)
                changed_y_vec = numpy.append(changed_y_vec,changed_y) 
                changed_x_vec = numpy.append(changed_x_vec,State.generation) 
                changed_line = live_plotter(changed_x_vec,changed_y_vec,changed_line,"Generations","Changed individuals","Changed individuals per generation") 
            plt.draw() 
            
            self.generation.setText(str(State.generation))
            self.generation.repaint()
            self.fitness.setText(str(fitness[index]))
            self.fitness.repaint()
            self.height.setText(str(population[index]['height']))
            self.height.repaint()
            self.items.setText(str(population[index]['items']))
            self.items.repaint()
            self.pm.setText(str(Config.p_m))
            self.pm.repaint()
            if (fitness[index] > Config.first and fitness[index] < Config.second):
                image = first
            elif (fitness[index] > Config.second and fitness[index] < Config.third):    
                image = second
            elif (fitness[index] > Config.third and fitness[index] < Config.forth):
                image = third
            elif (fitness[index] > Config.forth and fitness[index] < Config.fifth):
                image = forth
            elif (fitness[index] > Config.fifth):
                image = fifth   
            if (image != previmage):
                previmage = image
                self.character.setPixmap(image)

            population = GA.replacement(population, fitness)
            State.generation += 1


        fitness = GA.fitness(population)
        best_match_idx = numpy.where(fitness == numpy.max(fitness))
        index = best_match_idx[0][0]
        self.generation.setText(str(State.generation))
        self.generation.repaint()
        self.fitness.setText(str(fitness[index]))
        self.fitness.repaint()
        self.end.setText("Finished!")
        self.end.repaint()


def finished(GA, population, fitness, index):
    finish = False
    if (Config.kicking):
        return kicking_finished(population, fitness, index)
    if (Config.max_generations):
        finish = finish or max_generations_finished()
    if not finish and (Config.structure):
        finish = finish or structure_finished(GA, population, fitness, index)
    if not finish and (Config.content):
        finish = finish or content_finished(fitness, index)
    if not finish and (Config.near_optimal):
        finish = finish or near_optimal_finished(fitness, index)
    return finish        

def max_generations_finished():
    return State.generation >= Config.num_generations

def structure_finished(GA, population, fitness, index):
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    if(len(changed) == 0):
        return True
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    fitness_changed = GA.fitness(changed)
    best_match_idx_changed = numpy.where(fitness_changed == numpy.max(fitness_changed))
    index_changed = best_match_idx_changed[0][0]
    if ((fitness_changed[index_changed] - fitness[index]) < Config.delta_variation_fitness):
        return False    

    return True

def content_finished(fitness, index):
    if State.generation == 0:
        return False
    if (fitness[index] > State.best_fitness_current):
        State.best_fitness_current = fitness[index]
        State.consecutive_generations = 0
        return False
    else:
        State.consecutive_generations += 1
        return State.consecutive_generations >= Config.max_consecutive_generations     

def near_optimal_finished(fitness, index):
    if State.generation == 0:
        return False
    return (Config.optimal_fitness - fitness[index]) < Config.delta 

def kicking_finished(population, fitness, index):
    global changed
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    distance = Config.optimal_fitness - fitness[index]
    if  distance > Config.delta:        
        Config.kicking_flag = 1 
        return False

    return True

def live_plotter(x_vec,y1_data,line1,xlabel,ylabel,title,pause_time=0.1): 
    if line1==[]: 
        # this is the call to matplotlib that allows dynamic plotting 
        plt.ion() 
        fig = plt.figure() 
        ax = fig.add_subplot(111) 
        # create a variable for the line so we can later update it 
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)         
        #update plot label/title 
        plt.xlabel(xlabel) 
        plt.ylabel(ylabel) 
        plt.title(title) 
        plt.show() 
    line1.set_data(x_vec,y1_data) 
    # adjust limits if new data goes beyond bounds 
    if(numpy.min(y1_data)<=line1.axes.get_ylim()[0] or numpy.max(y1_data)>=line1.axes.get_ylim()[1]): 
        plt.ylim([numpy.min(y1_data)-numpy.std(y1_data),numpy.max(y1_data)+numpy.std(y1_data)]) 
    if(numpy.max(x_vec) >= line1.axes.get_xlim()[1]): 
        plt.xlim([numpy.min(x_vec)-numpy.std(x_vec),numpy.max(x_vec)+numpy.std(x_vec)]) 
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above 
    plt.pause(pause_time) 
     
    # return line so we can update it again in the next iteration 
    return line1 


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()    