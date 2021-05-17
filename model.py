# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:23 2021

@author: gaming
"""

import random
import matplotlib.pyplot
import agentframework
import csv
import numpy as np

#List the number of neighbours and seed
neighbourhood = 8  #for guiding D8 algorithm during distance calculation
seed = 1

#initialise the random number generator
random.seed(seed)

#attach number of agents and iterations the model will deal with
num_of_agents = 300
num_of_iterations = 100


#Lines here happen before any data is processed
environment =[]
agents =[]


# pull in hillslope heights from the text file
with open('snow.slope.txt', mode='r') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in file_reader:
        rowList = [] 
        for values in row:
            print(rowList)
            rowList.append(float(values))
        environment.append(rowList)
        line_count += 1


#create function
def distance_between(agents_row_a, agents_row_b):  

    return (((agents_row_a.x - agents_row_b.x)**2) +
            ((agents_row_a.y - agents_row_b.y)**2))**0.5
     
def print_agents():
    for i in range(num_of_agents):
        print(agents[i])

# Make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

print_agents()


# Move the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].share_with_neighbours(neighbourhood)
        
#check agents
print("After moving")
print_agents()

fig = matplotlib.pyplot.figure(frameon=(True))
ax = fig.add_axes([0, 0, 1, 1])

#plot elevation data in a graph
matplotlib.pyplot.ylim(0,299)
matplotlib.pyplot.xlim(0,299)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.title('Hillslope heights for a hilly area')
cbar=matplotlib.pyplot.colorbar(shrink=0.8)
cbar.set_label('Heights(meters)')
matplotlib.pyplot.savefig('Heights.png', dpi=300, bbox_inches='tight')
matplotlib.pyplot.show()


#Build dataset with slope gradients instead of slope heights
agents[i].x = np.linspace(0,np.pi*2,num_of_agents) 
agents[i].y = np.sin(agents[i].x) 
grads = np.gradient(agents[i].y) 

#Display gradients
fig, ax = matplotlib.pyplot.subplots()
ax.plot (agents[i].x, agents[i].y, "-b", label="values")
ax.plot (agents[i].x, grads, "--r", label="Gradients")
matplotlib.pyplot.legend()
matplotlib.pyplot.title('Gradients for a Hilly area')
matplotlib.pyplot.savefig('gradients.png', dpi=300, bbox_inches='tight')
matplotlib.pyplot.show()


#iterate over distances btn agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
      

      
    
