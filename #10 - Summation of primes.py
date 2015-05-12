#Project Euler problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#Written by: Ed Karwacki

x = 2
count = 1
sum = 2
for x in range (2,2000000):
        x += 1
        print x
        n=2
        isPrime = True
        for n in range (2, x-1):
                if isPrime == True:
                        if x % n == 0:
                                isPrime = False
        if isPrime == True:
                sum += x
                
print "sum is ",sum
