#!python3
import math
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""


def hypotenuse(a, b, c):
    side = 0
    if c:
        side = int(math.sqrt((a ** 2 + b ** 2)))
    elif not c:
        if a > b:
            side = int(math.sqrt((a ** 2 - b ** 2)))
        elif a < b:
            side = int(math.sqrt((b ** 2 - a ** 2)))
    return side


if __name__ == "__main__":
    assert hypotenuse(3, 4, True) == 5
    assert hypotenuse(5, 12, True) == 13
    assert hypotenuse(3, 5, False) == 4
    assert hypotenuse(13, 12, False) == 5
    
    