do {
    count = parseInt(prompt("Insert the number you like"));
    if (count > 0) {
        break;
    } else {
    }
} while (true);

function printPattern(symbol, times) {
    let pattern = "";
    for (let i = 0; i < times; i++) {
        pattern += symbol;
    }
    console.log(pattern);
}

for (let i = 1; i <= count; i++) {
    if (i % 2 === 1) {
        printPattern(" #", count / 2); 
    } else {
        printPattern("# ", count / 2); 
    }
}

console.log();
