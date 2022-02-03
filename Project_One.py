from random import choice 
#Project 1 ("The Lost Ant")
class RandomWalk():
    """A class to generate random walking of an Ant with no direction in particular."""
    def __init__(self, num_points = 50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        """calculate all the points in the walk charted"""
        #Keep taking steps until the point length is complete. 
        while len(self.x_values) < self.num_points:
            #decide the direction and how far
            #Choices are up, down, left, right & 1-4 steps.
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            #stop the moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            #calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
        

import matplotlib.pyplot as plt
#This part plots the movement of the Ant.
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values,c = "red", s=1)
plt.title("Charting Random Ant Walk", fontsize=20, fontname='Comic Sans MS')
plt.xlabel("X AXIS", fontsize=14)
plt.ylabel("Y AXIS", fontsize=14)
plt.show()
