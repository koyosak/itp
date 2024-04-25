do {
    count = parseInt(prompt("Insert the number you like"));
    if (count > 0) {
        break;
    } else {
        console.log("Please insert a positive number");
    }
} while (true);

function printPattern1(symbol, times) {
    let pattern = ""
    while (i < times) {
        console.log( " ")
        console.log("#")
    } i++
    console.log(pattern)
}

function printPattern2(symbol, times) {
    let pattern = ""
    while (i < times) {
        console.log("#")
        console.log(" ")
    } i++
    console.log(pattern)
}

while (i <= count) {
    if ( i % 2 == 2) {
        printPattern1()
    } else {
        printPattern2()
    }
    i++
}

console.log();