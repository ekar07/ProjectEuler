# Project Euler problem 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#Written by: Ed Karwacki
x=1
y=1
product = 0
for x in range (1,1000):
	for y in range(1,1000):
		a = x
		b = y
		c = 1000 - a - b
		if (a*a) + (b*b) == (c*c):
			product = a*b*c
			break
		y += 1
	x += 1
	
print "product is ",product