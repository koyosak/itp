#Phase4
#####I started the code based on the one I created on Phase3. At first, I tried to tile up my pattern manually.
	
	def draw():
    for x in range(0, 400, 40):
        for y in range(0, 400, 40):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            drawObject(x, y, 0.26)
        
#####While I was figuring out the number for scale, I noticed that I can calculate it by dividing pixel by 150.

#####I figured out the math and how to tile the pattern manually, however, I wasn't sure what elements I need to set the size of the cell based on what number I input. So I asked my roommate and he gave me good advices. He told me that I need the variable which set the size of the cell size. 

	    
    scale_number = #the number which determines the size of the cell

    spacing_x = width / scale_number
    spacing_y = height / scale_number
    #it determines the size of each cells
    
#####After I set it up, I used for loop to so that it automatically tile the pattern without make code for each pattern.

	    for i in range(scale_number):
        for j in range(scale_number):
            x = i * spacing_x
            y = j * spacing_y
            s = spacing_x / 150  #cell size / 150 is the number of s
            drawObject(x, y, s)    
    

#####Everything made sense for me and I thought I had everything I need to excute it, however, it didn't work. It only showed me the the background and the pattern didn't show. I was stuck in this situation and couldn't figure out what I was missing or what I did wrong. So I asked Rachel for help.
#####As soon as she saw my code, she knew what I was doing wrong. She gave me one hint. "in range is in integer, and you need float." I had to take time after the office hour to fully understand it. I did some research and found out that range can't take float. At that moment, I finally fully realize what Rachel was talking about. 
#####I found out that in range can't take float. But I didn't know how to change my code so that it can take float. There was no choice for me to avoid ChatGPT.... I askd ChatGPT what do I do to make my code compatible with float.

![My question](https://github.com/koyosak/itp/assets/157754438/3650cea9-fa30-439a-bd04-8db006808937)

![chatGPT answer](https://github.com/koyosak/itp/assets/157754438/e6d516b6-8519-41d1-902a-dc9f671cc516)

#####As you can see in the screenshot, it told me to create the function which works just like in range. So I did it in my code and it worked perfectly. The final version of my code is....

	def frange(start, stop, step):
    while start < stop:
        yield start
        start += step
        
	def draw():
    
    scale_number = 4.0

    spacing_x = width / scale_number
    spacing_y = height / scale_number
    

    for i in frange(0, scale_number, 1):
        for j in frange(0, scale_number, 1):
            x = i * spacing_x
            y = j * spacing_y
            s = spacing_x / 150 
            drawObject(x, y, s)

#####I don't like that I had to use chatGPT for the first time in my life. There are so much more I need to learn. I didn't know that in range can't take integer. Additionally, I noticed that someties I need to be creative and flexible. I didn't think that I needed to make the function which works the same like frange. I tend to stuck with the original was what I notice throughout this project. I'll gain more experience to understand how computer thinks and how to make code more efficient.