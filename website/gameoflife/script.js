// game of life

const grid = document.querySelector('.grid');
const gridSize = (75, 75);
let cells = [];

function createGrid() {
    for (let i = 0; i < gridSize; i++) {
        let row = []
        for (let j = 0; j < gridSize; j++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.addEventListener('click', () => toggleCell(i, j));
            grid.appendChild(cell);
            row.push(0);
        }
        cells.push(row);
    }
}

document.addEventListener("keydown", (e) => {
    if (e.key == "r") {
        randomize();
    }
    if (e.key == " ") {
        step()
    }
});

// render
function render() {
    // clear
    grid.querySelectorAll('.cell').forEach(cell => cell.style.backgroundColor = "");

    let i = 0;
    cells.forEach(row => {
        row.forEach(cell => {
            if (cell == 1) {
                grid.children[i].style.backgroundColor = "white";
            }
            i++;
        })
    })
}

function randomize() {
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            cells[i][j] = Math.round(Math.random());
        }
    }
    render();
}

function toggleCell(i, j) {
    cells[i][j] = cells[i][j] == 0 ? 1 : 0;
    render();
}

function step() {
    let newCells = [];
    for (let i = 0; i < gridSize; i++) {
        let newRow = [];
        for (let j = 0; j < gridSize; j++) {
            // check neighbors
            let sum = 0;
            for (let di = -1; di <= 1; di++) {
                for (let dj = -1; dj <= 1; dj++) {
                    if (!(di === 0 && dj === 0) && i+di >= 0 && i+di < gridSize && j+dj >= 0 && j+dj < gridSize) {
                        sum += cells[i+di][j+dj];
                    }
                }
            }

            switch (sum) {
                case 2:
                    newRow.push(cells[i][j]);
                    break;
                case 3:
                    newRow.push(1);
                    break;
                default:
                    newRow.push(0);
                    break;
            }
        }
        newCells.push(newRow);
    }
    cells = newCells;
    render();
}

createGrid();
render();