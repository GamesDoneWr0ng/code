const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const dimContainer = document.getElementById("dim_container");

var slice;
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

function getBombs(bombs, settings) {
    var result = NDArray.zeros(bombs.shape);
    for (let i = 0; i < settings["mines"].length; i++) {
        result.add(bombs.convolve(settings["mines"][i]["kernel"]))
    }
    return result;
}

function populateBombs(bombs, start, settings) {
    for (i=0;i<1000;i++){if (Math.random()<0.1) {bombs.arr[i] = 1;}}
    //bombs.set(0, ...start)
    return bombs;
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

    _indicies(flatIndex) {
        let indices = [];
        let step = this.size;

        for (let i=0; i < this.shape.length; i++) {
            step /= this.shape[i];
            const index = Math.floor(flatIndex / step);
            indices.push(index);
            flatIndex %= step;
        }
        
        return indices;
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

    max() {
        return this.arr.reduce((biggest, i)=>biggest>i?biggest:i)
    }

    // Custom get method for indexing (1D, 2D, etc.)
    get(...indices) {
        const slices = this._getSlices(...indices);
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

        if (result.length === 1) {
            return result[0];
        }

        return new NDArray(result, slices.filter(a=>a.length!==1).map(a=>a.length));
    }

    set(value, ...indices) {
        const slices = this._getSlices(...indices);

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
            if (other.shape === this.shape) {
                for (let i = 0; i<this.size; i++) {
                    this.arr[i] = this.arr[i] + other.arr[i];
                }
            }
            // idk what you do here. Math is hard.
            return;
        }
        // other is number (if you didnt fuck up dumbass)
        for (let i = 0; i<this.size; i++) {
            this.arr[i] = this.arr[i] + other;
        }
    }
    
    mul(other) {
        // other is NDArray
        if (other instanceof NDArray){
            if (other.shape === this.shape) {
                for (let i = 0; i<this.size; i++) {
                    this.arr[i] *= other.arr[i];
                }
            }
            // idk what you do here. Math is hard.
            return;
        }
        // other is number (if you didnt fuck up dumbass)
        for (let i = 0; i<this.size; i++) {
            this.arr[i] *= other;
        }
    }

    convolve(kernel) {
        // returns a new NDarray with the convolution of this NDArray and the kernel.
        for (let i = 0; i < kernel.shape.length; i++) {
            if (kernel.shape[i]%2 !== 1) {
                throw new Error("Kernel requires odd dimenstions got: " + kernel.shape);
            }
        }
        let result = new Array(this.size).fill(0);
        for (let i = 0; i < this.size; i++) {
            var indices = this._indicies(i);
            var thisSlice = NDArray.zeros(kernel.shape);
            for (let j = 0; j < thisSlice.size; j++) {
                if (kernel.arr[j] === 0) {continue;}
                var offset = thisSlice._indicies(j);
                offset = offset.map((a, b)=>a+indices[b]-Math.floor(thisSlice.shape[b]*0.5));
                thisSlice.arr[j] = this.get(...offset);
                for (let k = 0; k < offset.length; k++) {
                    if (offset[k] < 0 || offset[k] >= this.shape[k]) {
                        thisSlice.arr[j] = 0;
                        break;
                    }
                }
            }

            thisSlice.mul(kernel);
            result[i] += thisSlice.arr.reduce((a,b)=>a+b);
        }
        return new NDArray(result, this.shape);
    }
}

let settings = {
    "renderScale": 5,
    "squareSize": 30,
    "size": 10,
    "dims": 3,
    "shape": "Rectangle",
    "mines": [{
            "flag": flag,
            "open": 1, // TODO open bomb image
            "kernel": new NDArray([
                1,1,1,
                1,1,1,
                1,1,1,

                1,1,1,
                1,0,1,
                1,1,1,

                1,1,1,
                1,1,1,
                1,1,1
            ], [3,3,3])
        }
    ]
}

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
    drawGrid2D(opened, bombs, bombNumbers, slice)
}

function drawSVG(ctx, svg, x, y, transform=null) {
    if (transform === null) {
        transform = [settings["renderScale"],0,0,settings["renderScale"],0,0];
    }
    ctx.save();
    ctx.transform(transform[0]*settings["squareSize"]/svgWidth, transform[1], transform[2], transform[3]*settings["squareSize"]/svgWidth, transform[4]+x*settings["renderScale"], transform[5]+y*settings["renderScale"]);
    for (let index = 0; index < svg.length; index++) {
        ctx.fillStyle = svg[index][0];
        ctx.fill(svg[index][1]);
    };
    ctx.restore();
}

function drawGrid2D(opened, bombs, bombNumbers, slice) {
    let opened2D = opened.get(...slice);
    let bombs2D = bombs.get(...slice);
    let bombNumbers2D = bombNumbers.get(...slice);
    for (let row = 0; row < opened2D.shape[0]; row++) {
        for (let column = 0; column < opened2D.shape[1]; column++) {
            // absulute index of cell and least cursed line ever
            //let index = slice.map(a => a instanceof Slice ? (slice.reduce((total,x)=>total+(x instanceof Slice)) === 2 ? row : column): a);
            if (opened2D.get(row, column) === 1) {
                if (bombs2D.get(row,column) === 0) {
                    drawSVG(ctx, tileOpen, column*settings["squareSize"], row*settings["squareSize"]);
                    //getBombs(bombs, index).toString(), (column+0.5)*settings["squareSize"]*settings["renderScale"], (row+0.6)*settings["squareSize"]*settings["renderScale"]
                    ctx.fillText(bombNumbers2D.get(row,column).toString(), (column+0.5)*settings["squareSize"]*settings["renderScale"], (row+0.6)*settings["squareSize"]*settings["renderScale"]);
                } else {
                    drawSVG(ctx, tileClosed, column*settings["squareSize"], row*settings["squareSize"]);
                    drawSVG(ctx, flag, column*settings["squareSize"], row*settings["squareSize"])
                }
            } else {
                drawSVG(ctx, tileClosed, column*settings["squareSize"], row*settings["squareSize"]);
            }
            //drawSVG(ctx, flag, column*30, row*30);
        }
    }
}

function clickCanvas(canvas, event) {
    const rect = canvas.getBoundingClientRect();
    const x = Math.floor((event.clientX - rect.left) / settings["squareSize"]);
    const y = Math.floor((event.clientY - rect.top) / settings["squareSize"]);
    let index = Array(slice.length);
    let first = true;
    for (let i = 0; i < slice.length; i++) {
        if (slice[i] instanceof Slice) {
            index[i] = first ? y : x;
            first = false;
        } else {
            index[i] = slice[i]
        }
    }
    //index = slice.map(a => a instanceof Slice ? (slice.reduce((total,i)=>total+(i instanceof Slice)) === 2 ? x : y): a);
    opened.set(1, ...index);
    drawGrid2D(opened, bombs, bombNumbers, slice);
    console.log(x, y, index);
}

var sizes = Array(settings["dims"]).fill(settings["size"]);

canvas.width = sizes[0] * settings["squareSize"] * settings["renderScale"];
canvas.height = sizes[1] * settings["squareSize"] * settings["renderScale"];

ctx.textAlign = "center"
ctx.textBaseline = "middle"
ctx.font = (settings["squareSize"]*settings["renderScale"]).toString() + "px serif"

canvas.addEventListener("mousedown", function(e) {
    clickCanvas(canvas, e)
});

// create grid
var opened = NDArray.zeros(sizes);
var holes  = NDArray.zeros(sizes);
var bombs  = populateBombs(NDArray.zeros(sizes), [0,0,0], settings);
var bombNumbers = getBombs(bombs, settings);
var flags  = NDArray.zeros(sizes);

createDimSliders(settings);

//for (i=0;i<1000;i++){opened.arr[i] = 1;}
//console.log(bombNumbers.max())
