#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(num):
    answer = num % 2
    if answer == 0 or answer == 1:
        return True
    else:
        return False

x = isInteger(3)
print(x)

