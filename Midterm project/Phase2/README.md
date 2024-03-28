# Phase2

##### At first, I created the setup() which I learned from the example. I had particular color I wanted for the background in my mind, so I put the number of the color for the fill and tell it to color all of the background by using rect of the size of the canvas. I put stroke and set the color for it since I knew that I wanted stroke for my pattern. I also adjust the strokeWeight, but I did after I finished creating the pattern.
##### Secondly, I started thinking how to execute the pattern. I tried to use circle for the outer part of the petals, and bezierVertex for the inner part of it. 

	#the outer part of the petal
	def draw():
		fill(255)
		ellipse(75, 75, 150, 150)
		
	#one of the inner part of the petal
	beginshape()
	vertax(75, 159)
	bezierVertax(70, 120, 40, 80, 0, 75)
	endShape()
	#I used bezierVertax 4 times to create the petal kind of shape

##### By creating this code, I was able to make the shape of the pattern. However I couldn't use fill for the specific area I wanted the color. I was stuck in the situation. I tried to think from the scratch to re-build the code. I realized that I wanted the different color only for the petal part and using bezierVertax for all of the petal part might be better than using ellipse. It was just very simple thing now that I think about it. 
	#one of the petal part
	beginShape()
    vertex(75, 150)
    bezierVertex(70, 120, 40, 80, 0, 75)
    bezierVertex(0, 75, 0, 150, 75, 150)
    endShape()
    #I made 4 of it with different numbers
    
##### I've noticed that whenver I'm stuck with something, I tend to stick to the original code and try to make it work when there are other easier way to do. As I debug my own codes, I learned my tendencies and how to think flexible way.
