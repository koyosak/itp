# Final Project

## Create and design my website

[Final Project Website](https://koyosak.github.io/index.html)

# First page

## Set up the index.html

##### I started by writing emmet for HTML file. I just typed '!', and when I type the tab, it automatically creates one for you.

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Document</title>
	    *<link rel="stylesheet" href="visual.css" />
	</head>
	<body>
	    
	</body>
	</html>
	
##### I changed the document name to my name, and added * so that I can connect html to css.

### Navbar

##### Navbar (Navigation bar) is the list of links at the top of the page. I put my name as a logo, and two links which takes you to my background page and my work page in the navbar.

	    <nav class="navbar">
        <div class="navbar_container">
            <a href="#home" id="navbar__logo"> K o y o  S a k a t a</a>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"/>
            <div class="navbar__toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
            <ul class="navbar__menu"> 
                <li class="navbar__item">
                    <a href="/background.html" class="navbar__links" id="Background-page">Background<span></span></a>
                </li>
                <li class="navbar__item">
                    <a href="/mywork.html" class="navbar__links" id="My work-page">My work<span></span></a>
                </li>
            </ul>
        </div>
        
    
    </nav>
    
##### After I created the list for the navbar, I went to css file to make it look desent before I move on to next stuff.

##### I started with setting up with the box-sizing and margine to define the size of the screen, size and kinds of font, and the scroll-behavior.

	* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Optima',  sans-serif;
    scroll-behavior: smooth;
	}  

##### After that, I added the information of the size, color and font size, where I want to put texts. I also wanted the navbar to be visible even when you scroll down to the bottom, so I added those function as well (position:sticky;)

	.navbar {
    background: #051935;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2rem;
    position: sticky;
    top: 0;
    z-index: 999;

	}
	
	.navbar__container {
	    display: flex;
	    justify-content: space-between;
	    height: 100px;
	    z-index: 1;
	    width: 100%;
	    max-width: 1300px;
	    margin: 0 auto;
	    padding: 0 60px;
	}

##### I setted up the size, color of the list and logo, and how I want the cursor to be when it's on them. I also added hover so that the color of the link changes when the cursor touches it. I set the transition time as well. I had a reference video from Youtube, but it was quite different from what I wanted to do, so I took time to adjust and tweak around.

[Reference Video](https://www.youtube.com/watch?v=3-2Pj5hxwrw)

## Setting up the info bar

##### I wanted to have info bar at the bottom of the page, so I added the bar and my contact informations. I also used the website [Font Awesome](https://fontawesome.com/search) for the font of instagram and email as well.


	    <div class="info" id="about">
            <div class="info__container">
                <h1>Contact</h1>
                    <a href="/"><i class="fa-brands fa-instagram"></i> Instagram</a> <a href="/"><i class="fa-solid fa-envelope"></i> Email</a>
            </div>
        </div>

##### For CSS, I setted up the color of the font and the background color of the bar, and the font size. I also added the hover to change the color of the font when the cursor touches it, and set the transition time as well.

	.info {
    color: rgb(173, 179, 197);
    background-color: #051935;
    padding: 1.8rem 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
	}
	
	.info__container {
	    display: flex;
	    flex-direction: column;
	    margin: 20px;
	    width: 160px;
	    box-sizing: border-box;
	}
	
	.info__container a {
	    margin-bottom: 0.5rem;
	    color: rgb(107, 131, 138);
	    text-decoration: none;
	    transition: all 0.3s ease;
	}
	
	.info__container a:hover {
	    color: rgb(138, 196, 220);
	}
	
## Setting the background

#### After I created the frame of the page, I started working on with the background image. 

##### As much as I hated to put my face on the page, I chose to use my picture on the background of my website since it's my website. 

##### I struggled with adjusting the size of the image. There were some space on the side of the screen. The width of the navbar and the picture was never a same size no matter what I tried. I asked my roommate some help.

	.navbar {
    background: #051935;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2rem;
    position: sticky;
    top: 0;
    z-index: 999;

	}.navbar__container {
	    display: flex;
	    justify-content: space-between;
	    height: 100px;
	    z-index: 1;
	    width: 100%;
	    max-width: 1300px;
	    margin: 0 auto;
	    padding: 0 60px;
	}
	 .photo {
	    display: flex;
	    max-width: auto;
	    height: 100%;
	    justify-content: center;
	    align-items: center;
	} 

##### He realized that navbar had container and the photo didn't have it. He said you should create the container for the photo and try to match it to the navbar___container and see if it's gonna fix the issue.

	.photo-container {
    width: 100%; 
    display: flex;
    justify-content: center;
    align-items: center;
	}
	
	 .photo {
	    max-width: 100%;
	    height: auto;
	}
	
##### After few attempt with his help, I was managed to get the size of the photo right. 

## Working on the different page

### My work page
##### After I was satisfied with my homepage, I started working on with my work page. I was thinking of putting two screen scoring and sound design I did in the past on the page. I used google document to upload those video, and got the link by embed it, and put it to the HTML file.

##### Since I used the photo of me on the center, I wanted to have the video on each side. I tried to set the place of the video, but it was a little confusing. I struggled with changing the position of the video. I did a lot of research about CSS, and found the way out of the problem. I didn't use transform element to control the place of the video. It took me a day to get it right.

	.video1 {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    height: 30%;
    transform: translatey(70%);
    z-index: 1;
	}
	
	.video2 {
	    position: absolute;
	    top: 0;
	    left: 0;
	    width: 50%;
	    height: 30%;
	    transform: translatex(128%) translatey(70%);
	    z-index: 1;
	}

##### After I put the video, I found my face on the background to be very distracting. So I used overlay to tone down the background.

	.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%; 
    height: 106.6%;
    background-color: rgba(0, 0, 0, 0.5); 
	}

##### I wanted to have discription of the video on the top, so I added them and adjust the placement.

### Background page

##### For my background page, I wanted to have very sinple background information about me. I also wanted to change the background image, so I did that too.

##### When I added the background image, it looked fine. However, when I added the text on it, the extra space at the bottom of the image. I tried to tweak the size of the image and the container of the text, but I couldn't figure out how to fix it.

