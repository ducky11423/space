# Simulates an object approaching a planet in 1-dimension, pretends G and M are 1 because they are constant so who cares
import csv

distance = 100 #Initial distance
velocity = 0 #Intial velocity

timestep = 0.0011 #Number of seconds use for each step
totaltime = 0

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    writer.writerow(["Time", "Distance", "Velocity", "Acceleration"])
    writer.writerow([totaltime, distance, velocity, 0])
    while(distance > 0):
        acceleration = -1 / (distance ** 2)
        velocity += -acceleration * timestep
        distance += velocity * timestep
        totaltime += timestep
        writer.writerow([totaltime, distance, velocity, acceleration])

print("Reached planet in " + str(totaltime) + "s, " + str(totaltime/timestep) + " steps.")
