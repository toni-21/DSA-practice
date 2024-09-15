const testCase = "([{}])";

function findParentheses(test) {
    if (test.length === 0) {
        return true;
    }

    if (test.length % 2 !== 0) {
        return false;
    }

    var parens = { "{": "}", "(": ")", "[": "]" };
    var stack = [];

    for (var i = 0; i < test.length; i++) {
        const val = test[i];
        //check if the char is a left paren by checking if it exists as a key in parens
        if (parens[val]) {
            stack.push(val);
        } else {
            const leftBracket = stack.pop(val);
            const correctBracket = parens[leftBracket];
            if (val !== correctBracket) {
                return false;
            }
        }
    }

    if (stack.length !== 0) {
        return false;
    }

    return true;
}

const result = findParentheses(testCase);
console.log(`test case is `, result);