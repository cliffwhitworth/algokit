import math

def prob_pyramid(n: int)->None:
    length = n * 2 - 1
    mid = n - 1
    k = math.ceil(n/2)
    l = n - (k + mid - 1)
    oe = n % 2
    print(oe)

prob_pyramid(7)
