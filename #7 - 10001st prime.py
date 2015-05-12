#Project Euler Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#Written by: Ed Karwacki
x=2
count = 1
while count < 10001:
        x += 1
        isPrime = True
        n=2
        for n in range (2, x-1):
                if x % n == 0:
                        isPrime = False
                        break
        if isPrime == True:
                count += 1
print "10001 prime is ",x
                
