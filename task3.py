#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

def perimeter(numbers):
    answer = sum(numbers)
    return answer

x = perimeter([1,3,4])
print(x)
