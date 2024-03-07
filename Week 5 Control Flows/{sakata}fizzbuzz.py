for index in range(1, 100):
    if index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz") # I put this statement at last and it didn't work because computer priortize other two conditions and didn't aply this condition. I put this one first and now it's working.
    elif index % 3 == 0:
        print("Fizz")
    elif index % 5 == 0:
        print("Buzz")
    else:
        print(index)
    
print(index) # I tried to run this code without this last print(index) which actually excute this code. It didn't work at first but my roommate noticed that I didn't put it at last and pointed out for me. Now it's working.