import math
import numpy as np
import re

def string_reversal(s: str) -> str:
    """
    Enter a string
    Returns reversed string
    """
    return "".join(reversed(s))

s = "Hello World!"
# print("Reverse of \"{}\" is \"{}\"".format(s, string_reversal(s)))

def char_mapper(s: str) -> str:
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

    return maxchar


# print("Maxchar = {}".format(char_mapper(s)))

def array_slicer(arr: list, size: int) -> list:
    """
    Enter a list of integers and size of slices
    Returns list of slices
    """
    index = 0
    slices = []
    while (index < len(arr)):
        slices.append(arr[index:index + size])
        index += size

    return slices

arr = [1, 2, 3, 4, 5, 6, 7]
size = 2
# print(array_slicer(arr, size))

def anagrams(s: str) -> str:
    """
    Enter string
    Returns lowercase string stripped of whitespace and sorted
    """
    return "".join(sorted("".join(re.findall("\\S", s)).lower()))

a1 = "Eleven plus two"
a2 = "Twelve plus one"
# print("Strings are anagrams? {}".format(anagrams(a1) == anagrams(a2)))

def triangular_n(levels: int) -> None:
    """
    Enter number of levels as integer
    Prints a graphical representation of the triangular number
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

# triangular_n(5)

def is_triangular(n: int) -> bool:
    """
    Enter integer
    Returns bool if Triangular, (sqrt(1 + 8n) + 1) / 2 is an integer
    """
    return ((math.sqrt(1 + 8 * n) + 1) / 2).is_integer()

n = 21
# print("{} is a triangular number? {}".format(n, is_triangular(n)))

def prob_pyramid(n: int = 6) -> None:
    """
    Enter sides of dice (6) > 1 < 10
    Prints a pyramid of combinations of rolls of two dice
    """
    if n < 2 or n > 9:
        print("Number out of range")
        return
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

prob_pyramid(8)

def num_spirals(levels: int) -> None:
    """
    Enter number of levels
    Prints a matrix of spiraling count from 1 to n**2
    """
    cnt = 1
    startRow = 0
    endRow = levels - 1
    startCol = 0
    endCol = levels - 1
    matrix = np.zeros((levels, levels))
    # matrix = [[] for _ in range(levels)] 
    # for i in range(0, levels):
    #     matrix[i] = [0 for i in range(levels)]

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

# num_spirals(5)

# initialize memo outside of function
memo = dict()
def fib_recursion(n: int) -> int:
    """
    Enter integer n
    Returns Fibonacci number at index n
    """ 
    # If key value already exists return value
    if n in memo:
        return memo[n]

    if n < 2:
        return n

    # Add Fibonacci n - 1 with n - 2 using recursion and store in memo
    result = fib_recursion(n - 2) + fib_recursion(n - 1)
    memo[n] = result

    return result

def is_fibonacci(n: int) -> bool:
    """
    Enter an integer
    Returns bool 
    """
    if math.sqrt(5 * n**2 + 4).is_integer() or math.sqrt(5 * n**2 - 4).is_integer():
        return True

    return False 

# Use command-line interface
# n = input("Enter integer: ")
# print("Fibonacci number at index {} is {}".format(n, fib_recursion(int(n))))
# print("Is {} Fibonacci? {}".format(n, is_fibonacci(int(n))))

def neighbor_detector(s: str) -> None:
    """
    Enter a string with rows and cols of matrix shape 
        and 1s and 0s of length rows x cols
    Prints a string representing each index of input
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

s = " 3, 5, ; 110000000000111"
# neighbor_detector(s)

def geo_series(factor: float, start: int, span: int) -> None:
    """
    Enter a factor / probability and a value and range from that value
    Return the geometric mean
    """
    adjStart = start
    if start < 2:
        print("start must be >= 2")
    
    if span > 1:
        adjStart = 2

    series = 0
    for n in range(adjStart, start + span):
        # series += (n / (math.pow(2, n - 1)))
        series += n * math.pow(factor, n - 1)
        if n >= start:
            print("{}: {}".format(n, series))


# geo_series(.5, 5, 10)

def geo_mean(lst: list) -> None:
    print("{0:.2f}".format(math.pow(np.prod(lst), (1 / len(lst)))))

# geo_mean([1, 3, 9, 27, 81])

def is_geometric(lst: list) -> bool:
    if len(lst) <= 2:
        print("List must contain 3 or more numbers")
        return False

    ratio = lst[0] / lst[1]

    for i in range(2, len(lst)):
        if lst[i - 1] / lst[i] != ratio:
            return False
 
        return True

# print("Is geometric series? {}".format(is_geometric([1, 3, 9, 27, 81])))
