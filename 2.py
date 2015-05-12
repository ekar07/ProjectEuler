#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
first=1
second=2
x=0
sum = 2
count = 3
while second < 4000000:
        x = first + second
        if x % 2 == 0:
                sum += x               
        first = second
        second = x
        count += 1
print "sum is ",sum
