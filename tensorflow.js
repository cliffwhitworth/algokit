const tf = require('@tensorflow/tfjs');
// require('@tensorflow/tfjs-node');

function detectNeighbor(s) {
    const splt = s.split(";");

    // get rows and columns provided in s
    const shape = splt[0].match(/\d/g).map(Number);

    // get the elements of the array and turn them to 0 or 1 for slice sum
    const arr = splt[1]
        .match(/\D/g)
        .join("")
        .replace(/\s/g, "")
        .replace(/\*|./g,function(match) {return (match==".")?0:1;})
        .split("")
        .map(Number);

    // create matrix
    let matrix = tf.tensor2d(arr, shape);
    matrix.print();
    matrix = matrix.pad([[1,1],[1,1]]);
    const buffer = tf.buffer(matrix.shape, matrix.dtype, matrix.dataSync());

    let rtnstr = "";
    for (let i = 0; i <= shape[0] + 1; i++) {
        for (let j = 0; j <= shape[1] + 1; j++) {
            if (i != 0 && i != shape[0] + 1 && j != 0 && j != shape[1] + 1) {
                // if (matrix.slice([i, j], 1).as1D().dataSync()[0] == 1) {
                if (buffer.get(i, j) == 1) {
                    rtnstr += "*";
                } else {
                    let slice = matrix.slice([i-1, j-1], [3, 3]);
                    rtnstr += slice.sum().dataSync()[0];
                } 
            }           
        }
    }

    console.log(rtnstr)
}

// turn **..........*** into 3 x 5 matrix
// **...
// .....
// ..***
// iterate through matrix
// return string if element = * print * else print count of * nearby (1 up, down, sides, diags)
// e.g., **100233201***
s = " 3, 5 ; **..........*** "
const clean = tf.tidy(() => {
    detectNeighbor(s);
});

// Create a buffer and set values at particular indices.
// const buffer = tf.buffer([2, 2]);
// buffer.set(1, 0, 0);
// buffer.set(2, 0, 1);
// buffer.set(3, 1, 0);

// Convert the buffer back to a tensor.
// buffer.toTensor().print();

// Create a buffer and set values at particular indices.
// const a = tf.tensor1d([1, 2, 3, 4]);
// const buf = tf.buffer(a.shape, a.dtype, a.dataSync());
// buf.set(5, 0);
// buf.toTensor().print();

function tensorSpiral() {
    let nx = 5;
    let cnt = 1;
    let startRow = 0;
    let endRow = nx - 1;
    let startCol = 0;
    let endCol = nx - 1;
    let bufx = tf.buffer([nx, nx]);

    // use matrix to spiral n++ towards the middle
    while (startRow <= endRow && startCol <= endCol) {
    for (let i = startCol; i <= endCol; i++) {
        bufx.set(cnt, startRow, i);
        cnt++;
    }
    startRow++;
    for (let i = startRow; i <= endRow; i++) {
        bufx.set(cnt, i, endCol);
        cnt++;
    }
    endCol--;
    for (let i = endCol; i >= startCol; i--) {
        bufx.set(cnt, endRow, i);
        cnt++;
    }
    endRow--;
    for (let i = endRow; i >= startRow; i--) {
        bufx.set(cnt, i, startCol);
        cnt++;
    }
    startCol++;
    }

    bufx.toTensor().print()
}

tf.tidy(tensorSpiral);

console.log("Number of tensors in memory: %s", tf.memory().numTensors);

// Optional Load the binding:
// Use '@tensorflow/tfjs-node-gpu' if running with GPU.
// require('@tensorflow/tfjs-node');

// Train a simple model:
const model = tf.sequential();
model.add(tf.layers.dense({units: 100, activation: 'relu', inputShape: [10]}));
model.add(tf.layers.dense({units: 1, activation: 'linear'}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

const xs = tf.randomNormal([100, 10]);
const ys = tf.randomNormal([100, 1]);

model.fit(xs, ys, {
  epochs: 100,
  callbacks: {
    onEpochEnd: (epoch, log) => console.log(`Epoch ${epoch}: loss = ${log.loss}`),
    onTrainEnd: (log) => {
      console.log("Training End");
      xs.dispose();
      ys.dispose();
      model.dispose();
      console.log("Number of tensors: %s", tf.memory().numTensors);
    }
  }
});

console.log("Number of tensors: %s", tf.memory().numTensors);