var points = [];
var queries = [];
var dragPoint = -1;
var pointSize = 6;
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var lines = 8;
var drawNegative = false;
var maxLength = 1000;

const k_e = 8.99*10**9

const size = 600;
canvas.width = size;
canvas.heigth = size;

var chargeInputX = document.getElementById("c_x");
var chargeInputY = document.getElementById("c_y");
var chargeInputQ = document.getElementById("c_q");
var chargeInputBtn = document.getElementById("charge_btn");
var chargeList = document.getElementById("charges");

var queryInputX = document.getElementById("q_x");
var queryInputY = document.getElementById("q_y");
var queryInputBtn = document.getElementById("query_btn");
var queriesList = document.getElementById("queries");

chargeInputBtn.addEventListener("click", () => {
    points.push({x:chargeInputX.value, y:chargeInputY.value, q:chargeInputQ.value});
    let entry = document.createElement("li");
    entry.appendChild(document.createTextNode(`x: ${chargeInputX.value}, y: ${chargeInputY.value}, q: ${chargeInputQ.value}`));
    chargeList.appendChild(entry);
    draw();
});

queryInputBtn.addEventListener("click", () => {
    queries.push({x:queryInputX.value, y:queryInputY.value});
    let entry = document.createElement("li");
    let f = getForce(queryInputX.value, queryInputY.value);
    entry.appendChild(document.createTextNode(`x: ${queryInputX.value}, y: ${queryInputY.value}, f: ${Math.sqrt(f.x**2 + f.y**2)}N, θ: ${Math.atan2(f.y,f.x)}`))
    queriesList.appendChild(entry);
    draw();
});

canvas.onmousedown = function(e) {
    var pos = getPosition(e);
    dragPoint = getPointAt(pos.x, pos.y);
}

canvas.onmousemove = function(e) {
    if (dragPoint != -1) {
        var pos = getPosition(e);
        points[dragPoint].x = pos.x
        points[dragPoint].y = pos.y
        draw();
    }
    updateLists();
}

canvas.onmouseup = function(e) {
    dragPoint = -1;
}

function updateLists() {
    chargeList.childNodes.forEach((entry, i) => {
        entry.childNodes[0].textContent = `x: ${points[i].x}, y: ${points[i].y}, q: ${points[i].q}`;
    });
    queriesList.childNodes.forEach((entry, i) => {
        let f = getForce(queries[i].x, queries[i].y);
        entry.childNodes[0].textContent = `x: ${queries[i].x}, y: ${queries[i].y}, f: ${Math.sqrt(f.x**2 + f.y**2)*k_e}N, θ: ${Math.round(-Math.atan2(f.y,f.x)*180/Math.PI+180)}`;
    });
}

function getPosition(event) {
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
    return {x, y};
}

function getPointAt(x, y) {
    for (var i = 0; i < points.length; i++) {
        if (
            Math.abs(points[i].x - x) < pointSize &&
            Math.abs(points[i].y - y) < pointSize
    )
        return i;
    }
    return -1; 
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.heigth);
    if (points.length > 0) {
        for (var i = 0; i < points.length; i++) {
            if (points[i].q > 0 || drawNegative) {
                for (var theta = 0; theta < 2*Math.PI; theta += 2*Math.PI/lines) {
                    var x = points[i].x + pointSize * Math.cos(theta);
                    var y = points[i].y + pointSize * Math.sin(theta);
                    drawLine(x, y);
                }
            }
        }
    }

    ctx.lineWidth = 4;
    points.forEach((p) => {
        ctx.strokeStyle = p.q > 0 ? "red" : "blue";
        ctx.beginPath();
        ctx.arc(p.x, p.y, pointSize, 0, Math.PI * 2, true);
        ctx.stroke();
    });

    ctx.strokeStyle = "green";
    queries.forEach((p) => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, pointSize, 0, Math.PI * 2, true);
        ctx.stroke();
    });
}

function drawLine(x, y) {
    ctx.moveTo(x, y);
    ctx.strokeStyle = "black";
    ctx.beginPath();

    var t = 0;
    while (t < maxLength) {
        var f = getForce(x,y);
        var absF = Math.sqrt(f.x**2 + f.y**2)
        x += f.x/absF*-5;
        y += f.y/absF*-5;
        ctx.lineTo(x, y);
        t++;
    }
    ctx.stroke()
}

function getForce(x, y) {
    var f_x = 0;
    var f_y = 0;
    for (let i = 0; i < points.length; i++) {
        let d = Math.sqrt((x - points[i].x)**2 + (y - points[i].y)**2);
        let theta = Math.atan2(points[i].y-y, points[i].x-x);
        f_x += points[i].q / d**2 * Math.cos(theta);
        f_y += points[i].q / d**2 * Math.sin(theta);
    }
    //var f = Math.sqrt(f_x**2 + f_y**2);
    return {x:f_x, y:f_y};
}

draw()