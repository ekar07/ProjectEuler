# Project Euler - problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
#Written by: Ed Karwacki

d = 2
grid = [[0 for x in range(d)] for x in range(d)] 
count = 0

for row in range (0,d):
	for col in range (0,d):
		count += 1
		
print count
