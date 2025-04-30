const _funcName = "romanToInt";

const _compare = function(expected, actual) {
    return expected === actual;
}

// [result, ...inputs]
const _tests = [
    [3, "III"],
    [58, "LVIII"],
    [1994, "MCMXCIV"],
    [1, "I"],
    [4, "IV"],
    [9, "IX"],
    [40, "XL"],
    [90, "XC"],
    [400, "CD"],
    [900, "CM"],
    [3999, "MMMCMXCIX"],
    [1444, "MCDXLIV"],
    [444, "CDXLIV"],
    [888, "DCCCLXXXVIII"],
    [2023, "MMXXIII"],
    [14, "XIV"],
    [99, "XCIX"],
    [1666, "MDCLXVI"],
    [2000, "MM"],
    [2008, "MMVIII"],
    [1954, "MCMLIV"],
    [246, "CCXLVI"],
    [48, "XLVIII"],
    [5, "V"],
    [10, "X"],
    [50, "L"],
    [100, "C"],
    [500, "D"],
    [1000, "M"]
];

const _originalCode = `/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
};`;