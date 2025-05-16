const _funcName = "mySqrt";

const _compare = function(expected, actual) {
    return expected === actual;
}

// [result, ...inputs]
const _tests = [
    [0, 0],
    [1, 1],
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [2, 8],
    [3, 9],
    [3, 10],
    [3, 15],
    [4, 16],
    [4, 17],
    [4, 18],
    [4, 19],
    [4, 24],
    [5, 25],
    [5, 26],
    [5, 27],
    [5, 28],
    [5, 35],
    [6, 36],
    [6, 37],
    [6, 38],
    [6, 39],
    [1000, 1000000],
    [31622, 999999999]
];

const _originalCode = `/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    
};`;