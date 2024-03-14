#Powering

For a starting point, I put the template on the github to see how to excute. As I gave the definition for get_graph and get_power, I realised(it was wrong anyways) that I want to use the function of get_power for the variable of print_graph. So I put get_power function on the top so that computer reads it first.
####what I did
	def get_power(n)
		for i in range(-8, 9)
			i = (i^2)
			return(i)

	def print_graph(x):
		if x in range(9,1):
			print("*" * n)
		elif x in range(0,-8):
			print("*" * n)

	for n in range(-8,9):
		get power()
		print_graph()

	print()

######Looking back now, I realise that I shouldn't put same ("*" * n) with different condition. It might confuse the computer.

#####It gave me just the blank 18 lines. I wasn't sure what the problem was. I remember that my roommate told me to break down element by element when you de-bug. So I started break it down and try to see if each of the function works.

####range

	for n in range(-8,9):
		print(n)

	It gave me the line from -8 to 8.

	-8
	-7
	-6
	-5
	-4
	-3
	-2
	-1
	0
	1
	2
	3
	4
	5
	6
	7
	8


#####After that I tried different functions.

####get_power

	def get_power(i):
		i = i^2
		return(i)

	print(get_power(3))
	I put 3 to make sure that it's going to give me 9.

#####It gave me 1. I wasn't sure what the problem was. So I asked my roommate who knows coding better than me. He realised that ^ might not the syntax for square. So I fixed it to ** and it fixed the problem.

####Combination of range and get_power
#####After I saw that two things working correctly, I combined those 2 to see if it actually works.

	def get_power(i):
		i = i**2
		return(i)

	for n in range(-8,9):
		print(get_power(n))

	It gave me the exponentials of -8 to 9.

	64
	49
	36
	25
	16
	9
	4
	1
	0
	1
	4
	9
	16
	25
	36
	49
	64

#####After I saw that those two works correctly, I tried the last element of this coding, print_graph.

####print_graph

	def print_graph(x):
		x = "*" * x
		return(x)

	print(print_graph(3))

	It gave me ***

#####After I saw that print_graph works fine, I combine everything together. Also I realised that I can just use this simplified version of print-graph.

####Combination of 3 elements

	def get_power(i):
		i = i**2
		return(i)

	def print_graph(x):
		x = "*" * x
		return(x)

	for n in range(-8,9):
		get_power(n)
		print(print_graph)

	It gave me
	<function print_graph at 0x10ce5e550> 17 times.

#####The problem was that I thought I only have to put print-graph in print because I already put get-power function in the for loop. I stuck with this last step and asked my roommate again. He told me I have to put both of the def elements in print to make it work. So my final coding is....


	def get_power(i):
		i = i**2
		return(i)

	def print_graph(x):
		x = "*" * x
		return(x)

	for n in range(-8,9):
		get_power(n)
		print(print_graph(get_power(n)))

####Now that I look back
#####I realised that as I try to break down the steps, I find the way to make some of the part more simple. I think It also made the code more efficient. Additionally, by break down element by element, I started understanding more about the concept of de-bugging. I will keep trying to think in computer way because it's the most tricky part for me. 
