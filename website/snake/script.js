// Ai stuffs
const actor = tf.sequential();
actor.add(tf.layers.dense({ units: 30, activation: 'relu',  inputShape: [39] }));
actor.add(tf.layers.dense({ units: 20, activation: 'relu' }));
actor.add(tf.layers.dense({ units: 10, activation: 'relu' }));
actor.add(tf.layers.dense({ units: 4, activation: 'tanh' }));

const critic = new brain.NeuralNetwork({
    activation: 'sigmoid',
    hiddenLayers: [3],
    learningRate: 0.1
});

const optimizer = tf.train.adam(0.01);
const clippratio = 0.2;
const batchSize = 32;
const epochs = 10;
const moves = [[0,1], [0,-1], [1,0], [-1,0]];

// game of snake in javascript
const grid = document.querySelector('.grid');
const gridSize = 20;
let snake = [{x: 10, y:  10}, {x: 9, y:  10}, {x: 8, y:  10}];
let apple = {x: 15, y: 10};
let dx = 1;
let dy = 0;
let interval;
let score = 3;

// create grid
function createGrid() {
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            grid.appendChild(cell);
        }
    }
}

/* inputs listener for wasd
document.addEventListener('keydown', (e) => {
    if (e.key === 'w' && dy === 0) {
        dx = 0;
        dy = -1;
    } else if (e.key === 's' && dy === 0) {
        dx = 0;
        dy = 1;
    } else if (e.key === 'a' && dx === 0) {
        dx = -1;
        dy = 0;
    } else if (e.key === 'd' && dx === 0) {
        dx = 1;
        dy = 0;
    }
});*/

// move function for ai
function move(action) {
    const reward = 0;
    dx, dy = action;

    const head = {x: snake[0].x + dx, y: snake[0].y + dy};

    if (math.abs(head.x - apple.x) > math.abs(snake[0] - apple.x) ||  math.abs(head.y - apple.y) > math.abs(snake[0] - apple.y)) {
        reward += 0.1;
    } else {
        reward -= 0.1;
    }

    if (checkCollision(head)) {
        reset();
        reward -= 1;
    }

    snake.unshift(head);

    if (head.x === apple.x && head.y === apple.y) {
        generateApple();
        score++;
        document.getElementById("score").innerHTML = score;
        reward -= 1;
    } else {
        snake.pop();
    }

    render();
    return reward;
}

// render
function render() {
    // clear
    grid.querySelectorAll('.cell').forEach(cell => cell.style.backgroundColor = '');

    // snake
    snake.forEach(segment => {
        const cell = grid.children[segment.y * gridSize + segment.x];
        cell.style.backgroundColor = 'green';
    }
    )

    // apple
    grid.children[apple.y * gridSize + apple.x].style.backgroundColor = 'red';
}

// generate apple
function generateApple() {
    let valid = false;

    while (!valid) {
        apple.x = Math.floor(Math.random() * gridSize);
        apple.y = Math.floor(Math.random() * gridSize);

        valid = !snake.some(segment => segment.x === apple.x && segment.y === apple.y);
    }
}

// collision detection
function checkCollision(head) {
    if (head.x < 0 || head.x >= gridSize || head.y < 0 || head.y >= gridSize) {
        return true;
    }

    const snakeWithoutHead = snake.slice(1);

    return snakeWithoutHead.some(segment => segment.x === head.x && segment.y === head.y);
}

function reset() {
    snake = [{x: 10, y:  10}, {x: 9, y:  10}, {x: 8, y:  10}];
    apple = {x: 15, y: 10};
    dx = 1;
    dy = 0;
    score = 3;
    document.getElementById("score").innerHTML = score;
    render();
}

function collide(pos, state, length) {
    if (pos[0] === apple.x && pos[1] === apple.y) {
        state.push((2*length-1)/gridSize);
        state.push(1)
        return state, true;
    } else if (pos[0] < 0 || pos[0] >= gridSize || pos[1] < 0 || pos[1] >= gridSize) {
        state.push((2*length-1)/gridSize);
        state.push(-1)
        return state, true;
    } else {
        for (let k = 0; k < snake.length; k++) {
            if (pos[0] === snake[k].x && pos[1] === snake[k].y) {
                state.push((2*length-1)/gridSize);
                state.push(0)
                return state, true;
            }
        }
        return state, false;
    }
}

function getState() {
    let state = [];
    const directions = [[0,1], [1,2], [1,1], [2,1], [1,0], [2,-1], [1,-1], [1,-2], [0,-1], [-1, -2], [-1,-1], [-2, -1], [-1, 0], [-2, 1], [-1,1], [-1, 2]];

    for (let i = 0; i < directions.length; i++) {
        let pos = [snake[0].x, snake[0].y];
        for (let length = 1; length <= gridSize; length++) {
            if (Math.abs(directions[i][0]) + Math.abs(directions[i][1]) === 3) {
                let tempPos = [pos[0] + Math.floor(directions[i][0] / 2), pos[1] + Math.floor(directions[i][1] / 2)];
                state, changed = collide(tempPos, state, 2*length-1);
                if (changed) {
                    break;
                }

                pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]];
                state, changed = collide(pos, state, 2*length);
            } else {
                pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]];
                state, changed = collide(pos, state, length);
            }
            
            if (changed) {
                break;
            }
        }
    }

    state.push(snake[0].x/gridSize);                    // head x
    state.push(snake[0].y/gridSize);                    // head y

    state.push((apple.x - snake[0].x) / gridSize);      // relative apple x
    state.push((apple.y - snake[0].y) / gridSize);      // relative apple y

    state.push((snake[0].x - snake[snake.length - 1].x) / gridSize);  // relative tail x
    state.push((snake[0].y - snake[snake.length - 1].y) / gridSize);  // relative tail y

    state.push(score/gridSize);                         // length

    return state;
}

function argmax(array) {
    if (array.length === 0) {
      return -1; // Return -1 if the array is empty
    }
  
    let maxIndex = 0;
    let maxValue = array[0];
  
    for (let i = 1; i < array.length; i++) {
      if (array[i] > maxValue) {
        maxValue = array[i];
        maxIndex = i;
      }
    }
  
    return maxIndex;
  }

// mainLoop
function gameLoop() {
    const head = {x: snake[0].x + dx, y: snake[0].y + dy};

    if (checkCollision(head)) {
        clearInterval(interval);
        alert('Game Over');
        return;
    }

    snake.unshift(head);

    if (head.x === apple.x && head.y === apple.y) {
        generateApple();
        score++;
        document.getElementById("score").innerHTML = score;
    } else {
        snake.pop();
    }

    render();
}

createGrid()
//interval = setInterval(gameLoop, 150);

while (true) {
    const observations = []
    const actions = []
    const rewards = []
    for (let i = 0; i < batchSize; i++) {
        const state = tf.tensor2d(getState());
        const action = actor.predict(state);
        const reward = move(moves[argmax(action)]);
        observations.push(state);
        actions.push(action);
        rewards.push(reward);
    }

    const values = model.predict(tf.tensor2d(observations)).dataSync();
    const advantages = tf.tensor1d(rewards).sub(tf.tensor1d(values)).dataSync();
    const oldLogProbs = model.predict(tf.tensor2d(observations)).log().dataSync();

    for (let i = 0; i < epochs; i++) {
        const indices = tf.util.createShuffledIndices(batchSize);

        for (let k = 0; k < batchSize; k++) {
            const index = indices[k];
            obsTensor = tf.tensor2D([observations[index]]);
            actionTensor = tf.tensor2D([actions[index]]);
            rewardTensor = tf.tensor2D([rewards[index]]);
            advantageTensor = tf.tensor2D([advantages[index]]);
            oldLogProbsTensor = tf.tensor2D([oldLogProbs[index]]);

            const newLogProbTensor = actor.predict(obsTensor).log();
            const probRatioTensor = tf.exp(newLogProbTensor.sub(oldLogProbsTensor));
            const clippedRatioTensor = probRatioTensor.clipByValue(1 - clippratio, 1 + clippratio);
            const ppoLossTensor = tf.minimum(tf.mul(probRatioTensor, advantageTensor), tf.mul(clippedRatioTensor, advantageTensor)).neg();

            const valueTensor = actor.predict(obsTensor);
            const valueLossTensor = tf.square(rewardTensor.sub(valueTensor)).mean();

            const totalLossTensor = tf.add(ppoLossTensor, valueLossTensor);
            const gradients = tf.grads(totalLossTensor);
            const gradsAndVars = [
                [gradients[0].dataSync(), actor.trainableWeights]
            ];
            optimizer.applyGradients(gradsAndVars);
        }
    }
}