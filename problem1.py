#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(a,b,x):
    import math
    if x == True:
        ab = (a**2) + (b**2)
        answer = math.sqrt(ab)
        return answer
    if x == False:
        abc = []
        abc.append(a)
        abc.append(b)
        abc.sort()
        d = abc[0]
        e = abc[1]
        f = (e**2) - (d**2)
        answer = math.sqrt(f)
        return answer

k = hypotenuse(13,5,False)
print(k)
