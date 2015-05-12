#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
prime = 600851475143
factors = []
x = 2
for x in range (2,prime):
	if prime % x == 0:
		print x
	x += 1
