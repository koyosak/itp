def print_characters(character, count):
    while count > 0:
        print(character, end='')
        count -= 1
    
count = 0
while True: # I made boolian to make it clear for the computer because if/elif/else condition didn't work somehow (My roommate suggessted me to do it and how to break this loop using "break")
    count = int(input("Choose the number between 1 to 8"))
    if 1 <= count <= 8:
        break
    else: 
        print("Plese enter a number between 1 to 8")

for index in range(1, count + 1): # if I do count only, it'll make the pyramids for the given count -1 so I put + 1 so that it matches to the number you type in
    print_characters(' ', count - index)
    print_characters("#", index)
    print()
# I didn't put the last print() at first and it didn't work