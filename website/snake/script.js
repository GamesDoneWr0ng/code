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

// inputs listener for wasd
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
});

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
interval = setInterval(gameLoop, 150);