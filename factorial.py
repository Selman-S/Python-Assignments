'''Define a function named my_fact to calculate factorial of the given number. Given a non-negative integer return the factorial of the integer.

(Example: The factorial of 5 is: 5*4*3*2*1 = 120 and factorial of 0 is: 1)
For example:

Test	Result
print(my_fact(5))
120
print(my_fact(4))
24
print(my_fact(3))
6
'''

def my_fact(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum