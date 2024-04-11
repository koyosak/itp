# Phase3
##### Phase3 went smoother than Phase2 because I had the foundation code for my pattern. I followed the example on the gidhub and adopted to my pattern; define the drawObject function, using traslate and scale to change the place and the size of the pattern, and using push() and pop() to restore the function and separete it from draw() function. 
##### It was pretty clear for me to understand what I have to do. However, I somehow couldn't excute it. I broke down my code to piece by piece and checked every function. At first, I couldn't find the error in my code. 

	def setup():
    size(400, 400) 
    fill(137, 169, 255)
    rect(0, 0, 400, 400)
    stroke(25, 50, 160)
    strokeWeight(1.5)


	def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(255)
    
    beginShape()
    vertex(75, 150)
    bezierVertex(70, 120, 40, 80, 0, 75)
    bezierVertex(0, 75, 0, 150, 75, 150)
    endShape()
    #...abbr

    pop()
    
		def draw():
        	drawObject(0,0,1)
        	drawObject(0,200,1)
        	
##### It was very simple. I put the draw function with the tab and that was why it didn't execute my code correctly. I fixed it and it worked. I learned that when you debug your code, not only is it important to break down to see if the code actually works indivisually, but also to look at every detail and be careful to basic mistakes and errors.
