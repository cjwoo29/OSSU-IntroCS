# Finger Exercise Lecture 6
'''
Assume you are given an integer 0<= N <= 1000.
Write a piece of Python code that uses bisection search to guess N.
The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
Hints: If the halfway value is exactly in between two integers, choose the smaller one.
'''

N =333
count = 0
low = 0
high = 1000
ans = (low+high)//2

while ans != N:
    if ans<N:
        low = ans+1
    else:
        high = ans-1
    ans = (low+high)//2
    count += 1
print('count:', count)
print('answer:', ans)