# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:16:18 2021

@author: gaming
"""

import random

#create agent class

class Agent():
    
    def __init__(self, environment, agents):
        self.y = random.randint(0,299)
        self.x = random.randint(0,299)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def __str__(self):
        return "x=" + str(self.x) +", y=" + str(self.y) +", store=" + str(self.store)
        
    def move(self):
        """
        This modifies the x and y variables for the agent increasing or 
        decreasing them pseudorandomly.

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
     #claculate maximum slope in all raster cells using D8 algorithm    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist > neighbourhood:
            max = self.store >= agent.store
            maximum = max
            maximum >= self.store 
            maximum >= agent.store
            print("Maximum slope using D8 Algorithm " + str(dist) + " " + str(maximum))
   
    #distance between agents in a cell
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
    
 