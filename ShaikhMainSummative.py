#Mahaboob Ali Shaikh #COLLEGE
#January 25th 2017
#ICS3U1-03
#Description:A game where you collect 

#Importing the required Modules
import pygame
import random

#Initializing Pygame
pygame.init()
pygame.font.init()

#Making the constants
##COLORS##
BLACK=(0,0,0)
WHITE=(255,255,255)
SKY_GREY=(119,136,153)
BLUE=(0,68,255)
##COLORS##
##IMAGES##
RECYCLEMAN=pygame.image.load("Shaikhrecycle-man.png")#Size is 409px by 217px
GARBAGEBONE=pygame.image.load("Shaikhfishbones.png")#Size is 64px by 64px
HEART=pygame.image.load("Shaikhheart.png")#Size is 128px by 128px
##IMAGES##
##SOUND AND TEXT##
MENUSOUND = pygame.mixer.Sound("Shaikhstart.wav")
TEXT= pygame.font.SysFont("Century Gothica",75)
TEXT_INS= pygame.font.SysFont("Century Gothica",30)
##SOUND AND TEXT##
##SCREEN SIZE AND SURFACE##
SIZE=(800,600)
SCREEN= pygame.display.set_mode(SIZE)
FULL_X=800
FULL_Y=600
##SCREEN SIZE AND SURFACE

#Making the Variables
man_move_x=0#X-Value of Recycle man
man_move_y=350#Y-Value of Recycle Man
x_cord=random.randint(0,800)
y_cord=random.randint(0,600)
bone_move_y=0#Y-Value of the Fish
bone_move_x=200#X-Value of the fish
number_fishbones=3#How Many Fish are on the screen
heart_start=0 #Exit Condition
number_hearts=10 #Amount of hearts
caught=0#How many fish have been caught
go_down=1#How fast the fish are going
score=0#The highscore of the player


#List to hold the x and y co-ordinates(WIP)
garbagex=[]#Fish X-Value's
garbagey=[]#Fish Y-Value's


#Setting True and False for the right and left key, as well as making an end
#Case for the Garbage, Making sure also that the user can go into the loop.
#Also making sure the fish doesn't fall down too fast, along with the 
#main menu being able to be exited.
play_right=False
play_left=False 
garbage=False
playing = True
play=False
run= True
speed = True

#Making the def's
def spawn():
    global garbagex
    global garbagey
    global number_fishbones
    global garbage
    
    if garbage==False: #If the garbage got removed
        number_fishbones= random.randint(0,3)#Random Amount of respawing
        garbage=True#Making sure it doesn't go back into the loop
        for count in range(number_fishbones):#Respawing the Fish Again
                x_cord=random.randint(250,500)
                y_cord=random.randint(0,600)
                garbagex= garbagex + [x_cord]
                garbagey= garbagey + [y_cord]      

def draw(SCREEN):#Drawing all of the Fishes
    global garbagex
    global garbagey
    global number_fishbones
    
    pygame.draw.rect(SCREEN, SKY_GREY, (0,0,FULL_X,FULL_Y))
    pygame.draw.rect(SCREEN, BLACK, (0,500,800,600))
    for count in range(len(garbagey)):#Making sure only 3 fishes are being spawned.
        SCREEN.blit(GARBAGEBONE , pygame.Rect(garbagex[count],garbagey[count],10,10))    
    SCREEN.blit(RECYCLEMAN, pygame.Rect(man_move_x,man_move_y,100,217))
    
def main_menu():#The Main Menu
    
    pygame.draw.rect(SCREEN, BLUE, (0,0,FULL_X,FULL_Y))
    title_font=  TEXT.render("Recycle-Man Saves the Day!", 3, (255,255,255))
    left_font = TEXT.render("Press right to start" , 3, (255,255,255))
    right_font = TEXT.render("Press left for instructions", 3, (255,255,255))
    SCREEN.blit(title_font, pygame.Rect(100,100,400,600))
    SCREEN.blit(left_font, pygame.Rect(100,300,400,600))
    SCREEN.blit(right_font, pygame.Rect(100,500,400,600)) 
    pygame.display.flip()
    
def instruction_game():#The Instructions
    
    pygame.draw.rect(SCREEN, BLUE, (0,0,FULL_X,FULL_Y))
    explain_font = TEXT_INS.render("Instructions: Get the Fish and don't let your health be zero!" , 3, (255,255,255))
    instruction_font = TEXT_INS.render("Use the left and right arrow keys to catch them!", 3, (255,255,255))
    SCREEN.blit(explain_font, pygame.Rect(100,100,400,600))
    SCREEN.blit(instruction_font, pygame.Rect(100,300,400,600))
    pygame.display.flip()
    pygame.time.delay(5000)
    


#Starting the Main Game Loop
while run:
    
    main_menu()#Calling The Main Menu
    MENUSOUND.play(-1)
    
    for move in pygame.event.get(): #Start of movement checks
         
        if move.type == pygame.QUIT:
            run = False
            
        if move.type == pygame.KEYUP and move.key == pygame.K_RIGHT:
            play_right = False 
        
        if move.type == pygame.KEYUP and move.key == pygame.K_LEFT:
            play_left = False
    
        if move.type == pygame.KEYDOWN:
                
            if move.key == pygame.K_RIGHT:
                play_right = True  
                        
            if move.key == pygame.K_LEFT:
                play_left = True    

        #If the User Decides to Go straight into the game
        if play_right == True:
            play = True
            play_right = False
            run = False
        #If the user decides to check the Instructions First    
        if play_left == True:
            instruction_game()
            play_left= False
            play = True
            run = False
        #End of movement checks    

#Starting the Pre-Game Checks
if play == True:#Making sure that the user selected the game 
    spawn()
    
    for count in range(len(garbagey)):#Making sure the garbage spawns on top of the screen
        garbagey[count]=0
    #Starting the Game    
    while playing:
        
        if number_hearts <=0:#The Exit Solution
            pygame.draw.rect(SCREEN, SKY_GREY, (0,0,FULL_X,FULL_Y))
            die_font = TEXT.render(("YOU DIED m9!") , 3, (255, 255, 255))
            score_font = TEXT.render(("Your Score is: %i" %(score)) , 3, (255, 255, 255))
            SCREEN.blit(die_font, pygame.Rect(0,100,400,600))
            SCREEN.blit(score_font, pygame.Rect(0,50,10,10))
            pygame.display.flip()
            pygame.time.delay(2000)
            playing = False        
        
        if speed == False:#Making sure the loop occurs once.
                go_down += 0.2
                speed = True
        
        for count in range(len(garbagey)):
            garbagey[count]+=go_down #Adding one to the y-coordinate of the fishbone so it will go down.
        for count in range(len(garbagey)):
            if garbagey[count]>750:#Making sure the garbage despawn
                number_hearts-=1#Removing a health from Recycle-Man
                garbagey[count]=0
        
        #Movement Code   
        for move in pygame.event.get():
            
            if move.type == pygame.QUIT:
                playing = False
                
            if move.type == pygame.KEYUP and move.key == pygame.K_RIGHT:
                play_right = False 
            
            if move.type == pygame.KEYUP and move.key == pygame.K_LEFT:
                play_left = False
        
            if move.type == pygame.KEYDOWN:
                    
                if move.key == pygame.K_RIGHT:
                    play_right = True  
                            
                if move.key == pygame.K_LEFT:
                    play_left = True       
    
        
        #Moving the Actual Character
        if man_move_x >= 393:
            play_right = False
        elif man_move_x <=-93:
            play_left = False
            
        if play_right == True:
            man_move_x += 2
    
        if play_left == True: 
            man_move_x -= 2
        
        garbagex = garbagex[:3]#Making sure there is only 3 fishes
        garbagey = garbagey[:3]
        
        #Drawing the Screen
        draw(SCREEN)
        health_font = TEXT.render(("Health: %i" %(number_hearts)) , 3, (255, 255, 255))#Health of Recycle Man
        score_font = TEXT.render(("Score: %i" %(score)) , 3, (255, 255, 255))#Score of Recycle Man
        fast_font = TEXT.render(("Level: %0.1f" %(go_down)) , 3, (255, 255, 255))#Level of Recycle Man
        SCREEN.blit(health_font, pygame.Rect(0,10,10,10))
        SCREEN.blit(score_font, pygame.Rect(0,50,10,10))
        SCREEN.blit(fast_font, pygame.Rect(0,90,10,10))
        pygame.display.flip()
        
        #Collision Code
        for count in range(len(garbagey)):
            if garbagey[count] >= man_move_y and garbagey[count] <= (man_move_y+217):
                if garbagex[count] >= (man_move_x+50) and garbagex[count] <= (man_move_x+409):
                    x_cord=random.randint(200,600)#Respawning the fish
                    garbagex[count]=x_cord
                    garbagey[count]=0#Setting the Y-value to 0
                    caught+=1#Keeping track of the caught fishes
                    score+=50#The Score is kept track of
                    garbage=False#Respawning Garbage
                    if score%1000 == 0 and score != 0:#Making sure the speed-up only happen's once per 1000 points
                        speed = False
                    spawn()
                
    
            
#Quitting Pygame and Closing the Enitre Window
pygame.quit()