const arr1 = [1, 3, 6, 4, 1, 2]
const arr2 = [1, 2, 3]
const arr3 = [-1, -3]

function solution(arr) {
    arr.sort();
    let val = 1
    for (let i = 0; i < arr.length; i++) {
        const element = arr[i];
        if (element > 0) {
            if (i + 1 !== arr.length && arr[i + 1] - element > 1) {
                val = element + 1
                break
            } else if (i + 1 === arr.length) {
                val = element + 1
            }
        }
    }
    return val;
}

var ans = solution(arr1)
console.log('Answer is ', ans)