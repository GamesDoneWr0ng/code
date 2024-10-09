const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const dimContainer = document.getElementById("dim_container");

const settings = {
    "shape": "Rectangle",
    "mines": [
    ]
}

const renderScale = 5;

var squareSize = 30;
var sizes = [10, 10, 10]; // generalize for n dimentions coward

canvas.width = sizes[0] * squareSize * renderScale;
canvas.height = sizes[1] * squareSize * renderScale;

ctx.textAlign = "center"
ctx.textBaseline = "middle"
ctx.font = (squareSize*renderScale).toString() + "px serif"

var color = "#FF0000";
const svgWidth = 76;
const tileClosed = [
    ["#FDFCFD", new Path2D("M0 0 h 76 v 76 h -76 Z")],
    ["#757575", new Path2D('M 76,0 v 76 h -76 Z')],
    ["#b9b9b9", new Path2D("M 8.5,8.5 H 67.5 L 67.5,8.5 V 67.5 L 67.5,67.5 H 8.5 L 8.5,67.5 V 8.5 Z")]
];

const tileOpen = [
    ["#757575", new Path2D("M0 0 h 76 v 76 h -76 z")],
    ["#B9B9B9", new Path2D("M1 1 h 74 v 74 h -74 z")]
]

const flag = [
    ["#000000", new Path2D("M 36,55.5 v -39 H 40 v 39 z")],
    ["#000000", new Path2D("M 28.571,51.625 h 18.857 v 5.5 h -18.857 z")],
    ["#000000", new Path2D("M 20.222,56.459 H 55.777 V 63.5 H 20.222 Z")],
    [color, new Path2D("M 40,13.875 19.375,27 40,40.125 Z")]
];

function createDimSliders() {
    for (let i = 0; i < sizes.length; i++) {
        const sliderGroup = document.createElement("div");
        sliderGroup.classList.add("slider-group");

        const label = document.createElement("label");
        label.textContent = "Dim: " + (i+1).toString();

        const slider = document.createElement("input");
        slider.setAttribute("type", "range");
        slider.setAttribute("min", 1);
        slider.setAttribute("max", sizes[i]);
        slider.setAttribute("value", 1);
        slider.id = "slider-" + i.toString();
        slider.oninput = getSliderValues;

        const checkbox = document.createElement("input");
        checkbox.oninput = getSliderValues;
        checkbox.type = "checkbox";
        checkbox.id = "exclude-" + i.toString();

        const checkboxLabel = document.createElement("label");
        checkboxLabel.id = "checkboxLabel-" + i.toString();
        checkboxLabel.textContent = "1";

        sliderGroup.appendChild(label)
        sliderGroup.appendChild(slider)
        sliderGroup.appendChild(checkbox)
        sliderGroup.appendChild(checkboxLabel)
        dimContainer.appendChild(sliderGroup)
    }
}

function getSliderValues() {
    const excluded = [];
    const result = [];

    for (let i = 0; i < sizes.length; i++) {
        const checkbox = document.getElementById("exclude-"+i.toString());
        if (checkbox.checked) {
            excluded.push(i);
        }
    }

    if (excluded.length !== 2) {
        ctx.clearRect(0,0, canvas.width, canvas.height);
        return;
    }

    for (let i = 0; i < sizes.length; i++) {
        const slider = document.getElementById("slider-" + i.toString());
        let val = parseInt(slider.value, 10);
        
        const label = document.getElementById("checkboxLabel-" + i.toString());
        label.textContent = slider.value;

        if (excluded.includes(i)) {
            result.push(all());
        } else {
            result.push(val-1);
        }
    }

    slice = result;
    drawGrid2D(opened, bombs, slice)
}

function drawSVG(ctx, svg, x, y, transform=null) {
    if (transform === null) {
        transform = [renderScale,0,0,renderScale,0,0];
    }
    ctx.save();
    ctx.transform(transform[0]*squareSize/svgWidth, transform[1], transform[2], transform[3]*squareSize/svgWidth, transform[4]+x*renderScale, transform[5]+y*renderScale);
    for (let index = 0; index < svg.length; index++) {
        ctx.fillStyle = svg[index][0];
        ctx.fill(svg[index][1]);
    };
    ctx.restore();
}

function drawGrid2D(opened, bombs, slice) {
    let opened2D = opened.get(slice);
    let bombs2D = bombs.get(slice);
    for (let row = 0; row < opened2D.shape[0]; row++) {
        for (let column = 0; column < opened2D.shape[1]; column++) {
            if (opened2D.get(row, column) === 1) {
                drawSVG(ctx, tileOpen, column*squareSize, row*squareSize)

                // least cursed line ever
                let index = slice.map(a => a instanceof Slice ? (slice.reduce((total,x)=>total+(x instanceof Slice)) === 2 ? row : column): a);
                ctx.fillText(getBombs(bombs, index).toString(), (column+0.5)*squareSize*renderScale, (row+0.6)*squareSize*renderScale);
            } else {
                drawSVG(ctx, tileClosed, column*squareSize, row*squareSize);
            }
            //drawSVG(ctx, flag, column*30, row*30);
        }
    }
}

function getBombs(bombs, indices) {
    return Math.floor(Math.random()*9);
}

function populateBombs(bombs, start, settings) {

}

class Slice {
    constructor(start = null, end = null) {
        this.start = start;
        this.end = end;
    }
}
const all=()=>new Slice();

class NDArray {
    constructor(arr, shape = null) {
        if (shape === null) {
            this.shape = this._getShape(arr);
            this.size = shape.reduce((a,b)=>a*b);
            this.arr = arr.flat(Infinity);
        } else {
            this.size = shape.reduce((a,b)=>a*b);
            if (this.size !== arr.length) {
                throw new Error("Provided shape does not match array length.");
            }
            this.arr = arr;
            this.shape = shape;
        }
    }

    // Static method to generate zeros
    static zeros(shape) {
        const size = shape.reduce((a, b) => a * b); // Total number of elements
        const zerosArray = new Array(size).fill(0);
        return new NDArray(zerosArray, shape);
    }

    _getShape(arr) {
        let shape = [];
        while (Array.isArray(arr)) {
            shape.push(arr.length);
            arr = arr[0];
        }
        return shape;
    }

    // Static helper to reshape a flat array into an ND shape
    static _reshape(array, shape) {
        if (shape.length === 0) return array;
        const [size, ...restShape] = shape;
        if (restShape.length === 0) {
            return array.slice(0, size);
        }
        let result = [];
        const step = array.length / size;
        for (let i = 0; i < size; i++) {
            result.push(NDArray._reshape(array.slice(i * step, (i+1) * step), restShape));
        }
        return result;
    }

    _index(indices) {
        let flatIndex = 0;
        let step = this.size;

        for (let i=0; i<this.shape.length; i++) {
            step /= this.shape[i];
            flatIndex += indices[i] * step;
        }

        return flatIndex;
    }

    _sliceToIndicies(slice, axisLength) {
        const start = slice.start !== null ? slice.start : 0;
        const end = slice.end !== null ? slice.end : axisLength;
        const indices = [];
        for (let i = start; i < end; i++) {
            indices.push(i);
        }
        return indices;
    }

    _getSlices(...args) {
        let indicesList = [];
        for (let i = 0; i < this.shape.length; i++) {
            if (i < args.length) {
                if (args[i] instanceof Slice) {
                    indicesList.push(this._sliceToIndicies(args[i], this.shape[i]));
                } else {
                    indicesList.push([args[i]]);
                }
            } else {
                indicesList.push(this._sliceToIndicies(all(), this.shape[i]));
            }
        }

        return indicesList;
    }

    // Custom get method for indexing (1D, 2D, etc.)
    get(...args) {
        const slices = this._getSlices(...args);
        const result = [];

        const recurse = (indexList, depth) => {
            if (depth === this.shape.length) {
                const flatIndex = this._index(indexList);
                result.push(this.arr[flatIndex]);
            } else {
                for (let i of slices[depth]) {
                    recurse([...indexList, i], depth+1)
                }
            }
        };

        recurse([], 0)

        return new NDArray(result, slices.filter(a=>a.length!==1).map(a=>a.length));
    }

    set(value, ...indices) {
        const slices = this._getSlices(...args);

        const recurse = (indexList, depth) => {
            if (depth === this.shape.length) {
                const flatIndex = this._index(indexList);
                this.arr[flatIndex] = value;
            } else {
                for (let i of slices[depth]) {
                    recurse([...indexList, i], depth+1)
                }
            }
        };

        recurse([], 0)
    }

    add(other) {
        // other is NDArray
        if (other instanceof NDArray){
            // difficult shit pray you dont need it
            return;
        }
        // other is number (if you didnt fuck up)


    }
}

// create grid
var opened = NDArray.zeros(sizes);
var holes  = NDArray.zeros(sizes);
var bombs  = NDArray.zeros(sizes);
var flags  = NDArray.zeros(sizes);

createDimSliders();

for (i=0;i<10;i++){opened.arr[i*101] = 1;}