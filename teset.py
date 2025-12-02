import math
def check_squareNumber2(x):
    i = math.isqrt(x)
    return (i*i == x)

print(check_squareNumber2(12))