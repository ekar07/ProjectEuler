#Project Euler problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#Written by: Ed Karwacki
import math

def isPrime(x):
        for i in range (2,x):
                if x%i == 0:
                     return False
        return True

n=2000000
square = int(math.sqrt(n))
nums = []
for x in range (0,n+1):
        nums.append(x)
nums[1] = 0
for x in range (2,square):
        if isPrime(x) == True:
                for num in range (x+1,n+1):
                        if nums[num] % x == 0:
                                nums[num] = 0
primesum = sum(nums)
print "sum is ",primesum
