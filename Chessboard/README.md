# Chessboard

### I struggled more than I thought for this assignment. I couldn't figure out how to excute it perfectly. I'll put 2 files on my repository, the one file which kind of worked and the another one which I tried to fix and couldn't make it work. 

Here is what I have.

## The initial plan

#### When I started this assignment, I was pretty sure that I will reference the pyramid assignment. I made the simple outline before I start working on this assignment.

- Ask the user to choose a number they like

- If it's positive number, go to the next code, if not ask the number again

-  Execute the chessboard by differenciate the rows by odd rows and even rows

#### For the first part of this code, I had to do some research because I wasn't very familier with javaScript language. 

	#In order to ask user to insert the number, I used prompt.
	
	do {
    count = parseInt(prompt("Insert the number you like"));
    if (count > 0) {
        break;
    } else {
    }
	} while (true);
	
	
#### For building chessboard part,

	#for setting the function
	-my roommate helped me figure out how to build pattern 
	- using i++ as the destination of the loop was tricky for me to understand at first
	
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
	
#### I thought it worked for a second and realized that it only works when you put odd number

	#When I put 5, it prints 5 rows, but it prints 6 cols.
	
	 # # #
	# # # 
	 # # #
	# # # 
	 # # #
	 
#### At this moment, I realized that I can't use this method which multiply " #" and " #" because it is impossible to make odd numbers of columes.

####I tried to fix it by creating each function for the odd and even rows.

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
	
####It just gave me the blank result. I was trying to tweaking the function around, however, I couldn't make it work.



	