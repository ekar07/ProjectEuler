#Project Euler - problem 16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
#Written by: Ed Karwacki

x = 2**1000
s = str(x)
sum = 0
for i in range (len(s)):
    sum += int(s[i])
print sum


