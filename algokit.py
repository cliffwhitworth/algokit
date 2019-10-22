import math
import numpy as np
import re

def stringReversal(s: str) -> None:
    """
    Enter a string
    Returns reversed string
    """
    print("".join(reversed(s)))

s = "Hello World!"
# stringReversal(s)

def charMapper(s: str) -> None:
    """
    Enter a string
    Returns the character that appears most
    """
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

    print("Maxchar = {}".format(maxchar))


# charMapping(s)

def arraySlicer(arr: list, size: int) -> None:
    """
    Enter a list of integers and size of slices
    Returns list of slices
    """
    index = 0
    slices = []
    while (index < len(arr)):
        slices.append(arr[index:index + size])
        index += size

    print(slices)

arr = [1, 2, 3, 4, 5, 6, 7]
size = 2
# arraySlicer(arr, size)

def anagrams(s: str) -> None:
    """
    Enter string
    Returns lowercase string stripped of whitespace and sorted
    """
    return "".join(sorted("".join(re.findall("\\S", s)).lower()))

a1 = "Eleven plus two"
a2 = "Twelve plus one"
# print("Strings are anagrams? {}".format(anagrams(a1) == anagrams(a2)))

def triangularN(levels: int) -> None:
    """
    Enter number of levels as integer
    Returns a graphical representation of the triangular number
    """
    Ocount = 0
    for i in range(levels):
        for j in range(levels):
            if j < i + 1:
                print("O", end="")
                Ocount += 1
            else:
                print(" ", end=" ")
        print()
    print("The triangular number, n(n+1)/2, nCk where n + 1 = 6 and k = 2, for {} is {}".format(levels, Ocount))

# triangularN(5)

def isTriangular(n: int) -> None:
    """
    Enter integer
    Return Bool if Triangular, (sqrt(1 + 8n) + 1) / 2 is an integer
    """
    print("{} is a triangular number? {}".format(n, ((math.sqrt(1 + 8 * n) + 1) / 2).is_integer()))

# isTriangular(21)

def numSpirals(levels: int) -> None:
    """
    Enter number of levels
    Return a matrix of spiraling count from 1 to n**2
    """
    cnt = 1
    startRow = 0
    endRow = levels - 1
    startCol = 0
    endCol = levels - 1
    matrix = np.zeros((levels, levels))
    # matrix = [[] for _ in range(levels)] 
    # for i in range(0, levels):
    #     levels[i] = [0 for i in range(levels)]

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

# numSpirals(5)

def fibRecursion(n: int) -> int:
    """
    Enter integer n
    Returns Fibonacci number at index n
    """
    # Use memoization
    memo = dict()
    
    # If key value already exists return value
    if n in memo:
        return memo[n]
    
    if n < 2:
        return n

    # Add Fibonacci n - 1 with n - 2 using recursion and store in memo
    result = fibRecursion(n - 2) + fibRecursion(n - 1)
    memo[n] = result

    return result

def isFibonacci(n: int) -> None:
    if math.sqrt(5 * n**2 + 4).is_integer() or math.sqrt(5 * n**2 - 4).is_integer():
        return True

    return False 

# Use command-line interface
# n = input("Enter integer: ")
# print("Fibonacci number at index {} is {}".format(n, fibRecursion(int(n))))
# print("Is {} Fibonacci? {}".format(n, isFibonacci(int(n))))

def neighborDetector(s: str) -> None:
    """
    Enter a string with rows and cols of matrix shape 
        and 1s and 0s of length rows x cols
    Return a string representing each index of input
        if 1 a 1, if 0, how many 1s are 1 unit neighbors
        above, below, to the left / right, and each diagonal
    """
    arr = s.split(";")
    rows, cols = [int(d) for d in re.findall("\\d", arr[0])]
    matrix = np.asarray([int(c) for c in re.findall("\\S", arr[1])]).reshape(rows, cols)  
    print(matrix)  
    
    # Make a square filter, 1x1 = 1, 2x2 = 2, etc.    
    filter = 1
    matrix = np.pad(matrix, filter, "constant")
    for x, y in np.ndindex(matrix.shape):
        if (x != filter - 1 and x != rows + filter 
                and y != filter - 1 and y != cols + filter):
            if matrix[x,y] == 1:
                print("1", end="")
            else:
                print("".join([str(c) for c in matrix[x-filter:x+filter+1,y-filter:y+filter+1]
                        .ravel()]).count("1"), end="")

# s = " 3, 5, ; 110000000000111"
# neighborDetector(s)





