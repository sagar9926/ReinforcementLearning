import pygame
import random

pygame.init()

gameScreen = pygame.display.set_mode((1200,554)) #always pass tuple , this creates canvas where object resides

white = [255,255,255]
black = [0,0,0]
red = [255,0,0]

#Setting Game display dimensions
display_width = 1200
display_height = 554
gameClose =False
lead_x = display_width/2 #300  # Starting position of snake
lead_y =display_height/2 #300 # Starting position of snake
lead_x_change = 0
lead_y_change = 0


size_of_block = 1 #by how much coordinate of snake should change
FPS =  100
clock = pygame.time.Clock()


# Loading Car Image
carImg = pygame.image.load('C:\\Users\\sagar.agrawal\\Downloads\\EndGame\\framework_tutorial-master\\car.png')

carImg = pygame.transform.scale(carImg, (20, 20))

# Loading Destination Image
DestImg = pygame.image.load('C:\\Users\\sagar.agrawal\\Downloads\\EndGame\\framework_tutorial-master\\destination.jpg')
DestImg = pygame.transform.scale(DestImg, (30, 30))

#Adding Car image to canvas
def car(x,y):
    gameScreen.blit(carImg, (x,y))

def Destination(x,y):
    gameScreen.blit(DestImg, (x,y))

    
#Adding Map to our game
map_image = pygame.image.load('C:\\Users\\sagar.agrawal\\Downloads\\EndGame\\framework_tutorial-master\\map1.png').convert()
map_rect = map_image.get_rect()


#Random destination on road
while True:
    destination_x = random.randrange(0,display_width - size_of_block)
    destination_y = random.randrange(0,display_height - size_of_block)
    
    if map_image.get_at((destination_x,destination_y)) == (0, 0, 0, 255):
        print(destination_x)
        print(destination_y)
        print(map_image.get_at((destination_x,destination_y)))
                
        break
    else:
        continue
    
    
#Rotate car.
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
 

pygame.display.set_caption("OldSnake")


while not gameClose:
    for event in pygame.event.get():#event is something that user do
        print(event) # this will return the mouse movement
        if event.type == pygame.QUIT:
            gameClose = True
        if event.type == pygame.KEYDOWN: #Use pygame.KEYDOWN and pygame.KEYUP to detect if a key is physically pressed down or released. 
            # Now check if keydown was arrow key
            # x direction motion
            if event.key == pygame.K_LEFT:
                lead_x_change = -1*size_of_block #will get updated every time a key is pressed
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = size_of_block
                lead_y_change = 0
            #y direction motion
            elif event.key == pygame.K_UP:
                lead_y_change = -1*size_of_block #will get updated every time a key is pressed
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = size_of_block
                lead_x_change = 0
            elif event.key == pygame.K_ESCAPE:
                carRect = carImg.get_rect()
                topleft = carRect.topleft()
                blitRotateCenter(gameScreen, carImg, topleft, 2)
                
      
    # Adding Boundary conditions          
    #if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
       # gameClose = True
        
    if lead_x< 5:
        lead_x = 5
    elif lead_x > display_width - 5:
        lead_x = display_width - 5
        
    if lead_y< 5:
        lead_y = 5
    elif lead_y > display_height - 5:
        lead_y = display_height - 5
        
        
    # Changing destination position every time car reaches 
    if((lead_x > (destination_x-20) and lead_x < (destination_x + 20)) and (lead_y > (destination_y-20) and lead_y < (destination_y+20))):
        #Random destination
        #Random destination on road
        while True:
            destination_x = random.randrange(0,display_width - size_of_block)
            destination_y = random.randrange(0,display_height - size_of_block)
    
            if map_image.get_at((destination_x,destination_y)) == (0, 0, 0, 255):
                print(destination_x)
                print(destination_y)
                print(map_image.get_at((destination_x,destination_y)))
                break
            else:
                continue

        


             
    lead_x +=lead_x_change
    lead_y += lead_y_change

     
    gameScreen.fill(white)# set the background as white
    
    
    ## draw background image to game
    gameScreen.blit(map_image, map_rect)
    
    
    
    # Adding destination pointer to canvas
    Destination(destination_x,destination_y)
    
    # Adding car to canvas
    car(lead_x,lead_y)
    
    
    clock.tick(FPS) #reducing frame per second to 30
    #pygame.draw.rect(gameScreen,black,(lead_x,lead_y,10,10)) # X,y,width,height # draws a rectengle on game screen
    pygame.display.update() # needed when added any object like we added white background in previous line
    #pygame.quit()
    #quit()
            
    

