#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(numbers):
    numbers.sort()
    answer = numbers[-1]
    return answer

x = largest([1,5,3])
print(x)
