#Project Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Written by: Ed Karwacki
n = False
x=0
while n == False:
        x += 1
        if x % 1 == 0:
                if x % 2 == 0:
                        if x % 3 == 0:
                                if x % 4 == 0:
                                        if x % 5 == 0:
                                                if x % 6 == 0:
                                                        if x % 7 == 0:  
                                                                if x % 8 == 0:
                                                                        if x % 9 == 0:
                                                                                if x % 10 == 0:
                                                                                       if x % 11 == 0:
                                                                                               if x % 12 == 0:
                                                                                                       if x % 13 == 0:
                                                                                                               if x % 14 == 0:
                                                                                                                       if x % 15 == 0:
                                                                                                                               if x % 16 == 0: 
                                                                                                                                       if x % 17 == 0:
                                                                                                                                               if x % 18 == 0:
                                                                                                                                                       if x % 19 == 0:
                                                                                                                                                               if x % 20 == 0:
                                                                                                                                                                       print x
                                                                                                                                                                       n = True
                                                                                                                                                                
                                                                                                                                                                
