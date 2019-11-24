import re
def anagram(s: str) -> str:
    return ''.join(sorted(re.findall('\\S', s.lower())))

a1 = 'Eleven plus two'
a2 = 'Twelve plus one'
print(anagram(a1))
print(anagram(a2))
print(anagram(a1) == anagram(a2))