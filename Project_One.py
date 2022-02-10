from random import choice 
#Project 1 ("The Lost Ant")
class RandomWalk():
    """A class to generate random walking of an Ant with no direction in particular."""
    def __init__(self, num_points = 500000):
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
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c = point_numbers,cmap=plt.cm.Reds,
        edgecolor='none', s=15)
#Making the start and end easier to track.
    plt.scatter(0, 0, c="green", edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none',
        s=100)
    plt.title("Charting Random Ant Walk", fontsize=20, fontname='Times New Roman')
    plt.xlabel("X AXIS", fontsize=14)
    plt.ylabel("Y AXIS", fontsize=14)
    plt.show()
    
    keep_running = input("Make another ant walk? (Y?N): ")
    keep_running = keep_running.lower()
    if keep_running == "n":
        print("Thank you for participating in my program. - Cody ")
        break
