#Project Euler Problem 6
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Written by: Ed Karwacki
x=1
sum = 0
sumOfSquares = 0
for x in range (1,101):
        sumOfSquares += (x*x)
        sum += x
        x += 1
squareOfSums = (sum * sum)
if sumOfSquares > squareOfSums:
        total = sumOfSquares - squareOfSums
else:
        total = squareOfSums - sumOfSquares
print sumOfSquares, " - ", squareOfSums, " = ", total
        
