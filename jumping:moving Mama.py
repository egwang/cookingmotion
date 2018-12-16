import pygame 
pygame.init()

screenWidth = 520
margin = screenWidth//100
screenHeight = 700
win = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Cookin Motion")

#global class attributes of sprite
x = 0 #(x,y) positions of the sprite
y = screenHeight - 100
spriteSize = 50
vel = 20 #how fast sprite moves

run = True
isJump = False
leftMamaWalk = False
rightMamaWalk = False


jumpCount = 10 # how much we want the sprite to jump
walkCount = 0

walkRightList = [pygame.image.load('images/ManRight/R1.png'), pygame.image.load('images/ManRight/R2.png'), pygame.image.load('images/ManRight/R3.png'), pygame.image.load('images/ManRight/R4.png'), pygame.image.load('images/ManRight/R5.png'), pygame.image.load('images/ManRight/R6.png'), pygame.image.load('images/ManRight/R7.png'), pygame.image.load('images/ManRight/R8.png'), pygame.image.load('images/ManRight/R9.png')]

walkLeftList = [pygame.image.load('images/ManLeft/L1.png'), pygame.image.load('images/ManLeft/L2.png'), pygame.image.load('images/ManLeft/L3.png'), pygame.image.load('images/ManLeft/L4.png'), pygame.image.load('images/ManLeft/L5.png'), pygame.image.load('images/ManLeft/L6.png'), pygame.image.load('images/ManLeft/L7.png'), pygame.image.load('images/ManLeft/L8.png'), pygame.image.load('images/ManLeft/L9.png')]

bg = pygame.image.load('startpage/images/start.png')

mama = pygame.image.load('startpage/mamaAndSpatchula.png')
mama = pygame.transform.scale(mama, (spriteSize, spriteSize))



def redrawWindow(): #keeps redraw separate for good style
    global walkCount #global allows for updated count to also affect mainloop 
    win.blit(bg,(0,0))
    
    if walkCount + 1 >= 27: #there's 9 pics, so we display each pic 3 times
        walkCount = 0
    elif leftMamaWalk == True:
        win.blit(walkLeftList[walkCount//3], (x,y)) #changes picture every 3 frame
    
        walkCount += 1
    elif rightMamaWalk == True:
        win.blit(walkRightList[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(mama, (x,y))
    #win is where the rect is drawn onto
    #pygame takes in RGB Values
    #rectangles take in 4 values (x, y, width and height)
    pygame.transform.scale(mama,(500,500))
    pygame.display.update() #must update for the dispaly to show the rect
    

#mainloops should be separate than redrawAll
while run: 
    pygame.time.delay(27) #frame rate
    
    for event in pygame.event.get(): #event.type only works for 1 time things; ie: quit
        if event.type == pygame.QUIT: #top left red button 
            run = False
    
    #to get continuous motion (ie: moving left), follow the syntax below:
    keys = pygame.key.get_pressed() 
    print(x)
    if keys[pygame.K_LEFT] and x > 0 - margin:
        x -= vel
        leftMamaWalk = True
        rightMamaWalk = False
        
    elif keys[pygame.K_RIGHT] and x < screenWidth - spriteSize - margin:
        x += vel                        
        leftMamaWalk = False
        rightMamaWalk = True
    else:
        walkCount = 0

        
    if not(isJump): #doesn't allow you to move up/down if jumping or jump again if jumping
        if keys[pygame.K_SPACE] and x > 0 and x <= screenWidth - spriteSize - margin:
            isJump = True
            leftMamaWalk = False
            rightMamaWalk = False
            walkCount = 0
            
    else: #when jumping
        if jumpCount >= -10: 
            neg = 1 #start moving up 
            if jumpCount < 0:
                neg = -1 # moving down in the parabola
            #makes a quadratic parabola to illustrate diff speeds
            #0.5 scales the jump smaller 
            y -= 0.5* (jumpCount ** 2) * neg 
            jumpCount -= 1 #change heights
        else:
            isJump = False
            jumpCount = 10
            
    redrawWindow()
print("window closed!")           
pygame.quit() #closes the window