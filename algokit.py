import math
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

def arraySlices(arr: list, size: int) -> None:
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
# arraySlices(arr, size)

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
    level = ""
    Ocount = 0
    for i in range(levels):
        for j in range(levels):
            if j < i + 1:
                level += "O"
                Ocount += 1
            else:
                level += " "
        print(level)
        level = ""
    print("The triangular number, n(n+1)/2, nCk where n + 1 = 6 and k = 2, for {} is {}".format(levels, Ocount))

# triangularN(5)

def isTriangular(n: int) -> None:
    """
    Enter integer
    Return Bool if Triangular, (sqrt(1 + 8n) + 1) / 2 is an integer
    """
    print("{} is a triangular number? {}".format(n, ((math.sqrt(1 + 8 * n) + 1) / 2).is_integer()))

isTriangular(21)
