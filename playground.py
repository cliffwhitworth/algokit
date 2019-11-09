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

def fib(n: int) -> int:
    if n in cache:
        return cache[n]
    
    if n < 2:
        return n

    result = fib(n-2) + fib(n-1)
    cache[n] = result
    return result

cache = {}
# print(fib(8))

import math
def is_fibonacci(n: int) -> bool:
    return (math.sqrt(5 * n * n -4)).is_integer() or (math.sqrt(5 * n * n +4)).is_integer()

# print(is_fibonacci(21))
# for i in range(1, 100):
#     if is_fibonacci(i):
#         print("{} is fibonacci".format(i))

import re
import numpy as np
def neighbor_detector(s: str) -> str:
    splt = s.split(";")
    rows, cols = [int(d) for d in re.findall("\\d+", splt[0])]
    matrix = np.asarray([str(c) for c in re.findall("\\S", splt[1])]).reshape(rows, cols)
    print(matrix)
    matrix = np.pad(matrix, 1, "constant")
    rtnstr = ""
    for x, y in np.ndindex(matrix.shape):
        if x != 0 and x != rows + 1 and y != 0 and y != cols + 1:
            if matrix[x, y] == "*":
                # print("*", end="")
                rtnstr += "*"
            else:
                # print([str(c) for c in matrix[x-1:x+2,y-1:y+2].ravel()].count("*"), end="")
                rtnstr += str([str(c) for c in matrix[x-1:x+2,y-1:y+2].ravel()].count("*"))

    return rtnstr
    

s = " 3, 5, ;**..........***"
print(neighbor_detector(s))

