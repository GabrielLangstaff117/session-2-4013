import sys, pygame, math
from turtle import window_height, window_width

## Setup code

pygame.init()

x = 100
y = 100
dx = 0
dy = 0
Aim = True
Par1 = 0

## Initialise all variables here
##SizeA = int( window_height)
##SizeB = int( window_width)
##screen = pygame.display.set_mode((SizeA,SizeB))
screen = pygame.display.set_mode((800,800))

# Game loop



while True:
    # Event detection
    pos = pygame.mouse.get_pos()

    # This is necessary for being able to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and Aim == True:
            Par1 = Par1 + 1
            print("Par", Par1)
            x1 = pos[0]
            y1 = pos[1]
            dx = x1 -x
            dy = y1 -y
            Aim = False

    # Update game model

    x = x + dx
    y = y + dy

    # All drawing code goes here
    screen.fill((0,0,0))

 # amount    
 # colour, placement * spacing, size


    for i in range(210):
        for t in range(200):
            pygame.draw.circle(screen,(50, 200, 50),(i * 4, t*4), 2)
        
        
    for i in range(70):
        for t in range(70):
            pygame.draw.circle(screen,(1, 100, 1),(i * 12, t*12), 5)

    ##print(dx)
    ##print(dy)
    ##print(x)
    ##print(y)

    ##if x > 500:
    ##    print(x)

    if x >= 800:
        dx = -dx

    if y >=800:
       dy = -dy

    if x <= 1:
        dx = dx * -1

    if y <=1:
       dy = dy  * -1   

    if x >= 695 and x <= 705 and y >= 695 and y <= 705 and dx < 3 and dy < 3:
        print("Win")
        quit()

    dx = dx * 0.79
    dy = dy * 0.79

    if abs(dy) <= 0.1 and abs(dx) <=0.1:
        Aim = True

    if Aim == True:
        pygame.draw.circle(screen,(155,55,255),(pos),10) 
       ## x = pos
       ## y = pos
   
    pygame.draw.circle(screen,(255,255,255),(x,y),10) 

    pygame.draw.circle(screen,(100,30,30),(700,700),14) 
    pygame.draw.circle(screen,(30,30,30),(700,700),11)


    pygame.display.update()
