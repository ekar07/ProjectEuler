#Project Euler Problem 4
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Written by: Ed Karwacki
#!/usr/bin/python
import math   # This will import math module

x = 100
y = 100
product = 0
palindrome = []
for x in range(100,999):
	for y in range(100,999):
		product = x*y
		string = str(product)
		reverse = string[::-1]
		if string == reverse:
			palindrome.append(product)
		y += 1
	x += 1
largest = 0	
for n in palindrome:
        if int(n) > largest:
                largest = n
print largest
		
	
