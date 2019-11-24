const anagram = s => {
    return s.toLowerCase().match(/\S/g).sort().join('');
}

a1 = 'Eleven plus two';
a2 = 'Twelve plus one';
console.log(anagram(a1));
console.log(anagram(a2));
console.log(anagram(a1) === anagram(a2));
