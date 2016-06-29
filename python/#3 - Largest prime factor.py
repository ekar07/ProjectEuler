#Project Euler - Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Written by: Ed Karwacki
prime = 600851475143 
x = 2

while x *x < prime:
    while prime%x == 0:
        prime = prime / x
    x = x + 1

print "largest prime factor is ", prime
