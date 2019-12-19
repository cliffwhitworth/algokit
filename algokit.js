// Enter a string and return the reversed order
let s = "Hello World!"
function stringReversal(s) {
    return s.split("").reverse().join("");
    // return s.split("").reduce((a, b) => b + a, "");
}

// console.log(stringReversal(s));

// Enter a string, map and count the characters, return the character that occurs the most
function charMapper(s) {
    let arr = s.split("");
    let charmap = {};
    arr.forEach (function(c) {
        if (charmap[c]) {
            charmap[c]++;
        } else {
            charmap[c] = 1;
        }
    });

    let maxchar = '';
    let max = 0;
    for (let [key, value] of Object.entries(charmap)) {
        if (value > max) {
            maxchar = key;
            max = value;
        }
    }

    return maxchar;
}

// console.log(`Maxchar = ${charMapper(s)}`);

// Provide an array and size of slice and return an array of slices
function arraySlicer(arr, n) {
    let slices = [];
    let index = 0;
    while (index < arr.length) {
        slices.push(arr.slice(index, index + n));
        index += n;
    }

    return slices;
}

let arr = [1, 2, 3, 4, 5, 6, 7];
let size = 2;
// console.log("Array of slices: ", arraySlicer(arr, size));

// Check if two strings are anagrams
function anagrams(a) {
    return s.toLowerCase().match(/\S/g).sort().join("");
}

let a1 = "Eleven plus two";
let a2 = "Twelve plus one";
// console.log(`Are the strings anagrams? ${anagrams(a1) === anagrams(a2)}`)

// Enter a number of levels and create a staircase of #s
function triangularN(levels) {
    let level = "";
    let Ocount = 0;
    for (i = 0; i < levels; i++) {
        for (j = 0; j < levels; j++) {
            if (j < i + 1) {
                level += "O";
                Ocount++;
            } else {
                level += " ";
            }
        }
        console.log(level);
        level = "";
    }
    console.log(`Triangular number (n(n + 1) / 2), binomial coeff (nCk) where n(+1) = 6, k = 2 is ${Ocount}`);
    console.log()
    for (let i = 0; i < levels; i++) {
        for (let j = 0; j < levels; j++) {
            if (j < levels - i - 1) {
                level += " ";
            } else {
                level += "#";
            }
        }
        console.log(level);
        level = "";
    }
    console.log("Steps");
    console.log();
    for (i = 0; i < levels; i++) {
        for (j = 0; j < levels; j++) {
            if (j == i) {
                level += "1";
            } else {
                level += "0";
            }
        }
        console.log(level);
        level = "";
    }
    console.log("Identity Matrix")
}

// triangularN(5);

// See if (sqrt(1 + 8n) + 1) / 2 is an integer
function isTriangular(n) {
    return Number.isInteger((Math.sqrt(1 + 8 * n) + 1) / 2);
}

// for (let i = 0; i < 100; i++) {
//     if (isTriangular(i)) console.log(i);
// }

// Enter number of levels and print a pyramid of #s
function propPyramid(n) {
    const length = n * 2 - 1;
    const mid = n - 1;
    let level = '';
    let k = Math.ceil(n / 2);
    let l = n - (k + mid - 1);
    let oe = n % 2;
    let d = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < length; j++) {
            if (j < mid - i || j > mid + i) {
                level += '     ';
            } else {
                let m = j - i - k + 1;
                let p = j > mid?mid+l:j+l;
                if (i % 2 == 0) {
                    let q = j > mid?m+oe:k;
                    d = [q, p]
                } else {
                    let q = j > mid?m+1:k-oe;
                    d = [p+oe,q]
                }
                level += `[${d[0]},${d[1]}]`;
            }
        }
        if (i % 2 == 1) {
            k -= 1
            l += 1
        }
        console.log(level);
        level = '';
    } 
}

// let readline = require("readline").createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// readline.question("Enter number between 2 and 9: ", (n) => {   
//     if (n < 2 || n > 9) {
//         readline.close();
//         console.log('Input out of range');
//         return false;
//     }
//     propPyramid(n);
//     readline.close();
// });

// Enter levels and return a matrix of spiraling numbers
function numSpiral(levels) {
    let counter = 1;
    let startRow = 0;
    let endRow = levels - 1;
    let startColumn = 0;
    let endColumn = levels - 1;
    let matrix = [];

    for (let i = 0; i < levels; i++) {
        matrix.push([]);
    }

    while (startRow <= endRow && startColumn <= endColumn) {
        for (let i = startColumn; i <= endColumn; i++) {
            matrix[startRow][i] = counter;
            counter++;
        }
        startRow++;

        for (let i = startRow; i <= endRow; i++ ) {
            matrix[i][endColumn] = counter;
            counter ++;
        }
        endColumn--;

        for (let i = endColumn; i >= startColumn; i--) {
            matrix[endRow][i] = counter;
            counter++;
        }
        endRow--;

        for (let i = endRow; i >= startRow; i--) {
            matrix[i][startColumn] = counter;
            counter++;
        }
        startColumn++;
    }

    return matrix;
}

// console.log(numSpiral(5));

// Recursion example using Fibonacci. Get the nth number of the Fibonacci series using memoization
let memo = {};
function fibRecursion(n) {
    if (memo[n]) {
        return memo[n];
    }

    if (n < 2) {
        return n;
    }

    result = fibRecursion(n - 2) + fibRecursion(n - 1);
    memo[n] = result;

    return result;
}

let n = 8;
// console.log(`The number at position ${n} in the Fibonacci series is ${fibRecursion(n)}`);

// See if square root of (5 * n * n +- 4) is an integer
function isFibonacci(n) {
    return Number.isInteger(Math.sqrt(5 * n * n + 4)) || Number.isInteger(Math.sqrt(5 * n * n - 4));
}

// for (let i = 0; i < 100; i++) {
//     if (isFibonacci(i)) console.log(i);
// }

const tf = require('@tensorflow/tfjs');
const tensorSpirals = n => {
    const matrix = tf.buffer([n,n]);
    let count = 1;
    let startRow = 0;
    let endRow = n - 1;
    let startCol = 0;
    let endCol = n - 1;
    while(startRow <= endRow && startCol <= endCol) {
        for(let i = startCol; i <= endCol; i++) {
            matrix.set(count++, startRow, i);
        }
        startRow++;
        for(let i = startRow; i <= endRow; i++) {
            matrix.set(count++, i, endCol);
        }
        endCol--;
        for(let i = endCol; i >= startCol; i--) {
            matrix.set(count++, endRow, i);
        }
        endRow--;
        for(let i = endRow; i >= startRow; i--) {
            matrix.set(count++, i, startCol);
        }
        startCol++;
    }
    matrix.toTensor().print();
}

// tensorSpirals(5);

const mineDetector = s => {
    splt = s.split(';');
    let [rows, cols] = splt[0].match(/\d/g).map(Number);
    let strArr = splt[1].match(/\S/g).join('').replace(/\*|./g, c => {return c=='*'?1:0}).split('').map(Number);
    let temp = tf.tensor1d(strArr).reshape([rows,cols]).pad([[1,1],[1,1]]);
    rtnstr = ''
    for (x = 1; x <= rows; x++) {
        for (y = 1; y <= cols; y++) {
            if(temp.slice([x,y],[1,1]).dataSync() == 1) {
                rtnstr += '*'
            } else {
                rtnstr += temp.slice([x-1,y-1],[3,3]).sum().dataSync();
            }
        }
    }
    return rtnstr;
}

s = ' 3, 5, ; **..........*** ';
// console.log(mineDetector(s));

// Console line input
// let readline = require("readline").createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// readline.question("Enter number: ", (n) => {   
//     console.log(`${n} is Fibonacci? ${isFibonacci(n)}`)  
//     readline.close();
// });