const _funcName = "isValid";

const _compare = function(expected, actual) {
    return expected === actual;
}

// [result, ...inputs]
const _tests = [
    [true, "()"],
    [true, "()[]{}"],
    [false, "(]"],
    [false, "([)]"],
    [true, "{[]}"],
    [false, "("],
    [false, ")"],
    [false, "{"],
    [false, "}"],
    [false, "["],
    [false, "]"],
    [false, "((("],
    [false, ")))"],
    [true, "((()))"],
    [true, "(((())))"],
    [false, "((())"],
    [true, "([]())"],
    [true, "{[()]}"]
];

const _originalCode = `/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
};`;