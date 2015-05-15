#Project Euler problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#Written by: Ed Karwacki
import math
primesum = 2
n=2000000
nums = []
for x in range (0,n):
        nums.append(x)
square = int(math.sqrt(n))
for x in range (2,square):
        i = 2
        isPrime = True
        for i in range (2,x):
                if x%i == 0:
                     isPrime = False
                i += 1
        if isPrime == True:
                for num in range (x+1,n):
                        if nums[num] % x == 0:
                                #print nums[num]
                                del nums[num]
                                


        x += 1

print "done step 2"
primesum = sum(nums)
print "sum is ",primesum
