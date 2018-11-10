import pygame 
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Cookin Motion")

#global class attributes of sprite
x = 50 #(x,y) positions of the sprite
y = 300
width = 20
height = 20
vel = 20 #how fast sprite moves

run = True
isJump = False
jumpCount = 10 # how much we want the sprite to jump



def redrawWindow(): #keeps redraw separate for good style
    win.fill((255,255,255))
    #win is where the rect is drawn onto
    #pygame takes in RGB Values
    #rectangles take in 4 values (x, y, width and height)
    pygame.draw.rect(win, (255,0,0), (x,y, width,height))
    image = pygame.image.load("background.png")
    pygame.transform.scale(image,(500,500))
    win.blit(image, (0,0))
    pygame.display.update() #must update for the dispaly to show the rect
    

#mainloops should be separate than redrawAll
while run: 
    pygame.time.delay(100) #timer in the game
    
    for event in pygame.event.get(): #event.type only works for 1 time things; ie: quit
        if event.type == pygame.QUIT: #top left red button 
            run = False
    
    #to get continuous motion (ie: moving left), follow the syntax below:
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel:
        x += vel                        

    if not(isJump): #doesn't allow you to move up/down if jumping or jump again if jumping
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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
            
pygame.quit() #closes the window