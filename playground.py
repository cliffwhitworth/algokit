def reverse_string(s: str) -> str:
    return "".join(reversed(s))

s = "Hello World!"
# print(reverse_string(s))

def max_char(s: str) -> str:
    charmap = {}
    for c in s:
        if c in charmap:
            charmap[c] += 1
        else:
            charmap[c] = 1

    maxchar = ""
    max = 0
    for k, v in charmap.items():
        if v > max:
            maxchar = k
            max = v

    return maxchar

# print(max_char(s))

def array_slicer(arr: list, size: int) -> list:
    slices = []
    index = 0
    while index < len(arr):
        slices.append(arr[index:index+size])
        index += size

    return slices

arr = [1,2,3,4,5,6,7]
size = 2
# print(array_slicer(arr, size))

import re

def anagrams(s: str) -> str:
    rtn = "".join(sorted("".join(re.findall("\\S+", s)).lower()))
    print(rtn)
    return rtn

a1 = "Eleven plus two"
a2 = "Twelve plus one"
# print(anagrams(a1) == anagrams(a2))

def triangular(n: int) -> None:
    cnt = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if j < i:
                print("O", end="")
                cnt += 1
            else:
                print(" ", end="")

        print()

    print(cnt)

# triangular(6)

import math
def is_triangular(n: int) -> bool:
    return ((math.sqrt(1 + 8 * n) + 1) / 2).is_integer()

# for i in range(100):
#     if is_triangular(i):
#         print("{} is triangular".format(i))

def prob_pyramid(n: int) -> None:
    length = (n * 2) - 1
    midpoint = n - 1
    k = math.ceil(n / 2)
    l = n - (k + midpoint - 1)
    if n % 2 == 0:
        oe = 0
    else: 
        oe = 1
    d = []
    for i in range(n):
        for j in range(length):
            if j < midpoint - i or j > midpoint + i:
                print("     ", end="")
            else:
                m = j - i - k + 1
                p = midpoint + l if j > midpoint else j + l
                if i % 2 == 0:
                    d = [m + oe if j > midpoint else k, p]
                else:
                    d = [p + oe, m + 1 if j > midpoint else k - oe]

                print("[{},{}]".format(d[0],d[1]), end="")

        print()
        if i % 2 == 1:
            k -= 1
            l += 1
    
# prob_pyramid(6)

import numpy as np
def spiral_matrix(n: int) -> None:
    cnt = 1
    startRow = 0
    endRow = n - 1
    startCol = 0
    endCol = n - 1
    matrix = np.zeros([n, n])

    while startRow <= endRow and startCol <= endCol:
        for i in range(startCol, endCol + 1):
            matrix[startRow, i] = cnt
            cnt += 1
        startRow += 1
        for i in range(startRow, endRow + 1):
            matrix[i, endCol] = cnt
            cnt += 1
        endCol -= 1
        for i in range(endCol, startCol - 1, -1):
            matrix[endRow, i] = cnt
            cnt += 1
        endRow -= 1
        for i in range(endRow, startRow - 1, -1):
            matrix[i, startCol] = cnt
            cnt += 1
        startCol += 1

    print(matrix)

# spiral_matrix(5)

