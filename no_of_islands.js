let arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]];
for (let i = 0; i < arr.length; i++) {
    const row = arr[i];
    let s = ""
    for (let j = 0; j < row.length; j++) {
        const element = row[j];
        s += `${element} `
    }
    console.log(s)
}