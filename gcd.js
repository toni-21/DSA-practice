function gcd(x, y) {
    // Base case: If x is divisible by y, then y is the GCD
    if (x % y === 0) {
        return y;
    }
    // Recursive call with y as the dividend and x modulo y as the divisor
    return gcd(y, x % y);
}



function gdcOfList(arr) {
    // Initialize the GCD with the first element
    let result = arr[0];

    // Calculate the GCD for all remaining elements
    for (let i = 1; i < arr.length; i++) {
        result = gcd(result, arr[i]);
    }

    return result;
}

// Read the list of integers
const arr = [2, 4, 6, 8, 10];

// Print the GCD
console.log(gdcOfList(arr));