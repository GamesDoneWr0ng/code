const _funcName = "twoSum";

const _compare = function(expected, actual) {
    if (!Array.isArray(actual)) return false;
    actual.sort();
    if (expected.length !== actual.length) return false;
    for (let k = 0; k < expected.length; k++) {
        if (expected[k] !== actual[k]) return false;
    }
    return true;
}

// [result, ...inputs]
const _tests = [
    [[0,1], [2,7,11,15], 9],
    [[1,2], [3,2,4], 6],
    [[0,1], [3,3], 6]
];

const _originalCode = `/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
};`;

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateX(T, exclude1, exclude2) {
    let x;
    do {
        if (T >= 0) {
            const minX = T + 1;
            const maxX = 1e9;
            if (minX > maxX) {
                throw new Error("Invalid range for T >=0");
            }
            x = getRandomInt(minX, maxX);
        } else {
            const maxX = T - 1;
            const minX = -1e9;
            if (maxX < minX) {
                throw new Error("Invalid range for T <0");
            }
            x = getRandomInt(minX, maxX);
        }
    } while (x === exclude1 || x === exclude2);
    return x;
}

function generateTestCase() {
    const T = getRandomInt(-1e9, 1e9);
    let n;

    if (T === 1e9 || T === -1e9) {
        n = 2;
    } else {
        n = getRandomInt(2, 10000);
    }

    let i = getRandomInt(0, n - 1);
    let j = getRandomInt(0, n - 1);
    while (j === i) {
        j = getRandomInt(0, n - 1);
    }
    if (i > j) {
        [i, j] = [j, i];
    }

    const minA = Math.max(-1e9, T - 1e9);
    const maxA = Math.min(1e9, T + 1e9);
    const a = getRandomInt(minA, maxA);
    const b = T - a;

    const nums = new Array(n).fill(0);
    nums[i] = a;
    nums[j] = b;

    if (n > 2) {
        for (let k = 0; k < n; k++) {
            if (k === i || k === j) continue;
            nums[k] = generateX(T, a, b);
        }
    }

    return [[i, j].sort((x, y) => x - y), nums, T];
}

function generateTests(n) {
    const tests = [];
    for (let i = 0; i < n; i++) {
        tests.push(generateTestCase());
    }
    return tests;
}

var twoSum = function(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (seen.has(target - nums[i])) {
            console.log([i, seen.get(target - nums[i])].sort((a,b)=>a-b));
        }
        seen.set(nums[i], i);
    }
};

// Example usage:
const tests = generateTests(100);
//console.log(tests);

for (t of tests) {
    twoSum(...t.slice(1));
    console.log(t[0]);
    console.log("");
}