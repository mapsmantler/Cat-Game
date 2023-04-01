'''miscellaneous things'''


def drawcat(place, size):
    #function to draw the cat
    global catpic
    catpic = pygame.transform.scale(catpic, size)
    screen.blit(catpic, place)


def drawewaste(place, size):
    #function to draw ewaste
    global ewaste
    ewaste = pygame.transform.scale(ewaste, size)
    screen.blit(ewaste, place)


def pywritetextblock(place, textcolour, blockcolour, textt, size):
    #function for writing text in pygame + the box
    myFont = pygame.font.SysFont("Times New Roman", size)
    render = myFont.render(textt, 1, textcolour)
    fontSize = myFont.size(textt)
    rectangle = (place)

    textX = (rectangle[2] - fontSize[0]) // 2 + rectangle[0]  #centering
    textY = (rectangle[3] - fontSize[1]) // 2 + rectangle[1]
    textRect = (textX, textY, fontSize[0], fontSize[1])
    pygame.draw.rect(screen, blockcolour, rectangle)
    screen.blit(render, textRect)


def pywritetext(place, colour, textt, size):
    #function for writing solely text in pygame
    myFont = pygame.font.SysFont("Times New Roman", size)
    text = myFont.render(str(textt), 1, colour)
    screen.blit(text, place)


def colourfulbuttons(screen, colour, x1, y1, x2, y2, border, mx, my):
    # a function for the colouring the sides of the button
    if mx >= x1 and mx <= (x1 + x2) and my >= y1 and my <= (y1 + y2):
        pygame.draw.rect(screen, colour, (x1, y1, x2, y2), border)
'''
main draws
'''
def drawMENU(screen, currentstate, x, y, mx, my, button):
    #draws main menu
    screen.fill(BBYBLUE)
    pywritetextblock((200, 50, 400, 100), DRKBLUE, BLACK, "E-WASTE ELIMINATOR",
                     30)

    pywritetextblock((200, 200, 150, 100), DRKBLUE, BLACK, "PLAY", 30)
    colourfulbuttons(screen, NEON, 200, 200, 150, 100, 5, mx, my)

    pywritetextblock((450, 200, 150, 100), DRKBLUE, BLACK, "INSTRUCTIONS", 15)
    colourfulbuttons(screen, NEON, 450, 200, 150, 100, 5, mx, my)

    pywritetextblock((200, 350, 150, 100), DRKBLUE, BLACK, "LEADERBOARD", 15)
    colourfulbuttons(screen, NEON, 200, 350, 150, 100, 5, mx, my)

    pywritetextblock((450, 350, 150, 100), DRKBLUE, BLACK, "EDIT NAME", 17)
    colourfulbuttons(screen, NEON, 450, 350, 150, 100, 5, mx, my)

    pywritetextblock((700, 0, 100, 100), DRKBLUE, BLACK, "QUIT", 20)
    colourfulbuttons(screen, NEON, 700, 0, 100, 100, 5, mx, my)

    #checking if they clicked or no
    if button == 1:
        #to check if they want their name to be Anonymous Cat or not
        if x >= 200 and x <= 350 and y >= 200 and y <= 300 and name == "Anonymous Cat":
            currentstate = wait
        #if their name is already changed, they can go ahead
        elif x >= 200 and x <= 350 and y >= 200 and y <= 300 and name != "Anonymous Cat":
            currentstate = play
        #view instructions
        elif x >= 350 and x <= 600 and y >= 200 and y <= 300:
            currentstate = instruct
        #view the leaderboard
        elif x >= 200 and x <= 350 and y >= 350 and y <= 450:
            currentstate = leaderboard
        #create account
        elif x >= 350 and x <= 600 and y >= 350 and y <= 450:
            currentstate = createacc
        #exiting program
        elif x >= 700 and x <= 800 and y >= 0 and y <= 100:
            currentstate = exit

    return currentstate


'''
draw instructions, page 1 & 2
'''
def drawINSTRUCTIONS(screen, currentstate, x, y, button):
    global e
    #drawing instructions
    screen.fill(BBYBLUE)
    pygame.draw.rect(screen, DRKBLUE, (100, 50, 600, 400))
    pywritetext((120, 70, 200, 50), BLACK, "YOU ARE THIS:", 20)
    pywritetext((325, 70, 350, 50), BLACK, "YOUR OBJECTIVE IS TO SHOOT OR", 17)
    pywritetext((320, 100, 350, 50), BLACK, "EAT AS MANY E-WASTES AS YOU CAN.",
                17)
    pywritetext((350, 140, 100, 50), BLACK, "E-WASTES LOOK LIKE THIS:", 20)
    pywritetext((450, 250, 100, 100), BLACK, "The score is based off of", 15)
    pywritetext((450, 270, 100, 100), BLACK, "the amount of enemies slayed.",
                15)
    pywritetext((120, 330, 100, 100), BLACK, "You start off like this.", 14)
    pywritetext((300, 330, 100, 100), BLACK, "Your life decreases", 14)
    pywritetext((290, 350, 100, 100), BLACK, "if enemies get past you.", 14)
    pywritetextblock((620, 345, 50, 100), BLACK, GREEN, ">", 20)
    colourfulbuttons(screen, BLACK, 620 - 5, 345 - 5, 50 + 10, 100 + 10, 5, mx,
                     my)
    #added it on the outside because it looks prettier
    pywritetextblock((135, 400, 100, 40), BLACK, GREEN, "<<BACK", 20)
    colourfulbuttons(screen, BLACK, 135 - 5, 400 - 5, 100 + 10, 40 + 10, 5, mx,
                     my)

    screen.blit(fullhealth, (120, 250, 100, 100))
    screen.blit(notfullhealth, (290, 250, 100, 100))
    drawcat((135, 100, 500, 100), (100, 100))
    drawewaste((450, 175, 100, 100), (50, 50))
    if button == 1:
        #going to the next page
        if x >= 620 and x <= 670 and y >= 345 and y <= 445:
            currentstate = instruct2
        #going back to the menu
        if x >= 135 and x <= 235 and y >= 400 and y <= 440:
            currentstate = menu
    return currentstate


def drawINSTRUCTIONS2(screen, currentstate, x, y, button):
    #function for drawing the second page of instructions
    screen.fill(BBYBLUE)
    pygame.draw.rect(screen, DRKBLUE, (100, 50, 600, 400))
    pywritetextblock((100, 80, 600, 50), BLACK, DRKBLUE, "CONTROLS", 25)
    pywritetextblock(
        (100, 120, 600, 50), BLACK, DRKBLUE,
        "Use the < and > arrows keys or a & d to move left and right respectively.",
        15)
    pywritetextblock((100, 160, 600, 50), BLACK, DRKBLUE,
                     "Press the ^ arrow key, space, or w to shoot.", 15)
    pywritetextblock((500, 345, 50, 100), BLACK, GREEN, "<", 20)
    colourfulbuttons(screen, BLACK, 500, 345, 50, 100, 5, mx, my)
    pywritetextblock((580, 345, 100, 100), BLACK, GREEN, "START", 20)
    colourfulbuttons(screen, BLACK, 580, 345, 100, 100, 5, mx, my)
    pywritetextblock((100, 200, 600, 50), BLACK, DRKBLUE,
                     "After every 10 kills, the enemies fall faster.", 20)
    pywritetextblock((100, 250, 600, 50), BLACK, DRKBLUE,
                     "Scared? Wanna opt out? Press the surrender button.", 20)
    screen.blit(flagpic, (370, 300, 100, 100))
    if button == 1:
        #button for play
        if x >= 600 and x <= 700 and y >= 345 and y <= 445 and name != "Anonymous Cat":
            currentstate = play
        #as always, if their name is Anonymous Cat, ask if they want to change it
        if x >= 600 and x <= 700 and y >= 345 and y <= 445 and name == "Anonymous Cat":
            currentstate = wait
        #back button for first page
        if x >= 500 and x <= 550 and y >= 345 and y <= 445:
            currentstate = instruct
        #??menu??
        if x >= 700 and x <= 800 and y >= 0 and y <= 100:
            currentstate = menu

    return currentstate
    #if button was pressed, then it would be instruct1, if button was pressed, currentstate would be instruct


'''
play functions, moving, shooting, etc
'''
def drawWAIT(screen, currentstate, button, x, y):
    #warning the user if they don't have a custom name

    #first drawing the scene
    screen.blit(backgroundPic, (0, 0, 800, 500))
    screen.blit(catpic, (X, Y))
    for i in range(livesleft):
        screen.blit(livespic, (25 * i, 40, 100, 10))
    pointts = "Score: " + str(points)
    pywritetext((30, 30, 100, 10), BLACK, pointts, 20)

    #the actual message
    pygame.draw.rect(screen, DRKBLUE, (100, 100, 600, 300))
    pywritetextblock((100, 120, 600, 50), BLACK, DRKBLUE,
                     "You haven't made an account yet.", 25)
    pywritetextblock((100, 170, 600, 50), BLACK, DRKBLUE,
                     "Would you like to save your progress?", 25)
    pywritetextblock((100, 210, 600, 50), BLACK, DRKBLUE,
                     "You will be known as \'Anonymous Cat\' if you don't.",
                     20)
    pywritetextblock((150, 270, 200, 100), YT, BLACK, "I'm OK with that.", 15)
    colourfulbuttons(screen, NEON, 150, 270, 200, 100, 5, mx, my)
    pywritetextblock((450, 270, 200, 100), YT, BLACK,
                     "NOO I want my own name!", 13)
    colourfulbuttons(screen, NEON, 450, 270, 200, 100, 5, mx, my)

    #giving the user choices
    if button == 1:
        #choosing to continue/play
        if x >= 150 and x <= 350 and y >= 270 and y <= 370:
            currentstate = play
        #choosing to make an account
        if x >= 450 and x <= 650 and y >= 270 and y <= 370:
            currentstate = createacc
    return currentstate


def moving(screen, currentstate, button, x, y, scale):
    global e, myClock, catpic, backgroundPic, rightarrow, leftarrow, X, Y, points, livesleft, addedpoints, speed

    #drawing out the background and neccesary things
    screen.blit(backgroundPic, (0, 0, 800, 500))
    screen.blit(catpic, (X, Y))
    screen.blit(flagpic, (700, 0, 100, 100))
    for i in range(livesleft):
        screen.blit(livespic, (25 * i, 40, 100, 10))
    pointts = "Score: " + str(points)
    pywritetext((30, 30, 100, 10), BLACK, pointts, 20)

    myClock.tick(60)

    #the actual movement
    if X <= 10:
        if rightarrow == True:
            X += 10
    #restricters
    if X >= 680:
        if leftarrow == True:
            X -= 10

    #restricters
    if X >= 10 and X <= 680:
        if rightarrow == True:
            X += 10
        elif leftarrow == True:
            X -= 10

    playerrect = pygame.Rect(X, Y, 120, 120)

    #if the cat collides/eats the enemy, it deletes enemy and adds point
    if checkCollision(playerrect, enemyrect) == True:
        points += 1
        addedpoints += 1
        if addedpoints == 10:
            speed += 1
            addedpoints = 0
        enemy_xyvalue[-1] = 0
        enemy_xyvalue[-2] = random.randint(50, 650)


def shooting(screen, button, X, Y, collision):
    global missilestart, shotTimer, hasShot, going1, bullets, space, points, addedpoints, speed
    bulletrect = pygame.Rect(X, Y, 5, 10)

    #checking if the shooting up signal is up
    if space == True:
        bullets.append(X)  #adding new missile
        missilestart.append(400)
        space = False
    shotTimer = pygame.time.get_ticks()  # reset timer

    #marking enemyrect
    enemyrect = pygame.Rect(enemy_xyvalue[-2], enemy_xyvalue[-1], 50, 50)
    for i in range(len(missilestart) - 1, -1, -1):
        #start at index max, -1 as the exit, and -1 as the difference
        pygame.draw.rect(screen, BLACK, (bullets[i], missilestart[i], 5, 10),3)
        bulletrect = pygame.Rect(bullets[i], missilestart[i], 5, 10)
        #draw the missile
        missilestart[i] -= 10  # moves missle down(up the screen), by 5
        if missilestart[i] <= 0:
            del missilestart[i]
            del bullets[i]

        #if the bullet collides with the enemy, it refreshes the enemy and adds one point
        elif checkCollision(bulletrect, enemyrect) == True:
            del missilestart[i]
            del bullets[i]
            points += 1
            addedpoints += 1
            #speeds up after every 10 points
            if addedpoints == 10:
                speed += 1
                addedpoints = 0
            enemy_xyvalue[-1] = 0
            enemy_xyvalue[-2] = random.randint(50, 650)

    return bulletrect


#deletes the missile if it's out of the screen, aka at y = -1

#if pygame.time.get_ticks() - shotTimer >= 100: # 1 second difference


def checkCollision(playerrect, enemyrect):
    #function for checking collision
    if playerrect.colliderect(enemyrect) == True:
        return True
    else:
        return False


def initTarget():
    #initializing target at the start of the code, or whenever needed
    enemy_xyvalue = []
    enemy_xyvalue.append(random.randint(50, 650))
    enemy_xyvalue.append(0)
    return enemy_xyvalue


def drawEnemies(screen, enemy_xyvalue):
    global catpic, backgroundPic, livesleft, points, collision, speed, addedpoints, ewaste
    #function for drawing enemies
    screen.blit(ewaste, (enemy_xyvalue[-2], enemy_xyvalue[-1], 50, 50))
    enemyrect = pygame.Rect(enemy_xyvalue[-2], enemy_xyvalue[-1], 50, 50)
    #if the enemy goes off screen
    if enemy_xyvalue[-1] > 500:
        livesleft -= 1
        enemy_xyvalue[-1] = 0
        enemy_xyvalue[-2] = random.randint(50, 650)
    else:
        #enemy coming down
        enemy_xyvalue[-1] += speed

    return enemyrect


'''
leaderboard functions/database functions
'''
def drawLEADERBOARD(screen, currentstate, x, y):
    global rankings, username, score, amtslayed, largest, newamtslayed, newscore, newusername, points, openfile, page
    #function for drawing leaderboard
    #drawing out the leaderboard
    screen.fill(BBYBLUE)
    pygame.draw.rect(screen, YT, (725, 0, 75, 75))
    pywritetext((745, 0, 100, 20), BLACK, "X", 55)
    colourfulbuttons(screen, BLACK, 725, 0, 75, 75, 5, mx, my)
    yy = 50
    pywritetext((40, 20, 25, 20), BLACK, "Rankings", 15)
    pywritetext((150, 20, 25, 20), BLACK, "Username", 15)
    pywritetext((400, 20, 25, 20), BLACK, "Amount Slayed", 15)

    #rankings list, instead of making a seperate list, it utilizes indexs
    for i in range(len(amtslayed)):
        indexx = int(i) + 1
        pywritetext((40, yy + i * 30, i + i * 15, 20), BLACK,
                    indexx + page * 15, 20)

    #username list
    for i in range(len(username)):
        pywritetext((150, yy + i * 30, i + i * 15, 20), BLACK,
                    username[i + page * 15], 20)

    #amtslayed list
    for i in range(len(amtslayed)):
        pywritetext((400, yy + i * 30, i + i * 15, 20), BLACK,
                    amtslayed[i + page * 15], 20)

    #returning to menu
    if button == 1:
        if x >= 700 and x <= 800 and y >= 0 and y <= 100:
            currentstate = menu
    return currentstate


def organize():
    global amtslayed, username, pointslist, namelist, rankings, ranklist, name

    #organizing the list to put back into the file
    #it creates new lists from the old lists
    namelist = []
    pointslist = []
    ranklist = []
    added = False
    for i in range(len(amtslayed)):
        j = int(amtslayed[i])
        oldname = username[i]
        if points > j and added == False:
            #adding in new values
            added = True
            namelist.append(name)
            pointslist.append(points)
        #adding in old values
        namelist.append(oldname)
        pointslist.append(j)
    amtslayed = pointslist
    username = namelist


def writeinfo():
    #function for writing the lists into the data
    writedata = open("leaderboard.dat", "w")
    for i in range(len(username)):
        indexx = int(i) + 1
        writedata.write("%s," % str(indexx))
        writedata.write("%s," % username[i])
        writedata.write("%s," % amtslayed[i])

        writedata.write("\n")

    writedata.close()


'''
create account functions
'''
def writingtext(place, colour, size):
    global screen, inputtext, letter, backspace, keyreturn, keydown, name
    #for the writing text part in create account

    #initializing name as "Anonymous Cat"
    name = "Anonymous Cat"
    if keydown == True:
        if len(inputtext) < 11:
            if keyreturn == True:
                name = inputtext
                return name
                inputtext = ""
            # adding the unicode
            else:
                inputtext += letter
                letter = ""
    #pressing backspace
    if backspace == True:
        inputtext = inputtext[:-1]

    #drawing the actual scene
    pywritetext(place, colour, inputtext, size)
    pywritetextblock((0, 150, 800, 50), BLACK, BBYBLUE,
                     "Current number of characters: " + str(len(inputtext)),
                     20)
    pywritetext((570, 215, 800, 50), BLACK, "Press Enter to Continue.", 15)

    #putting a restricter on the amt of characters
    if len(inputtext) >= 11:
        pywritetextblock((250, 250, 300, 50), BLACK, BBYBLUE,
                         "Maximum Number of Characters Reached.", 20)
        pywritetext((250, 310, 200, 50), BLACK, "Please Delete 1+ Characters",
                    20)
        pywritetext((170, 350, 200, 50), BLACK,
                    "Orelse You Will Be Known As \'Anonymous Cat\'", 20)

    return name


def drawCREATEACC(screen, currentstate, x, y, button):
    global writingtextt, letter, name, keyreturn
    screen.fill(BBYBLUE)
    name = "Anonymous Cat"
    pywritetextblock((0, 50, 800, 50), BLACK, BBYBLUE,
                     "Please Enter Your Desired Username:", 30)
    pywritetextblock((0, 100, 800, 50), BLACK, BBYBLUE, "Maximum Length: 10",
                     20)

    pywritetextblock((730, 0, 70, 70), BLACK, YT, "X", 50)
    colourfulbuttons(screen, BLACK, 730, 0, 70, 70, 5, mx, my)
    pygame.draw.rect(screen, DRKBLUE, (230, 200, 330, 50))
    colourfulbuttons(screen, BLACK, 230, 200, 330, 50, 5, mx, my)
    if button == 1:
        if x >= 230 and x <= 560 and y >= 200 and y <= 250:
            writingtextt = True
    if writingtextt == True:
        pygame.draw.rect(screen, YT, (230, 200, 330, 50))
        name = writingtext((250, 200, 300, 50), BLACK, 25)
        if keyreturn == True:
            writingtextt = False
        elif currentstate != createacc:
            writingtextt = False
    return name


def drawScene(screen, mouse, enemy_xvalue):
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, mouse, 10)
    pygame.draw.circle(screen, BBYBLUE, enemy_xvalue, 30)
    pygame.display.flip()


'''death states'''
def drawDEATH(screen, currentstate, button, x, y):
    #function for drawing the state in which the user dies. RIP

    pygame.draw.rect(screen, DRKBLUE, (100, 100, 600, 350))
    pywritetextblock((100, 100, 600, 200), BLACK, DRKBLUE, "YOU DIED", 50)
    pywritetextblock((200, 300, 130, 100), DRKBLUE, BLACK, "MENU", 30)
    colourfulbuttons(screen, NEON, 200, 300, 130, 100, 5, mx, my)
    pywritetextblock((460, 300, 130, 100), DRKBLUE, BLACK, "RETRY", 30)
    colourfulbuttons(screen, NEON, 460, 300, 130, 100, 5, mx, my)
    #asking the user for an input
    if button == 1:
        #if the user were to press menu to go back
        if x >= 200 and x <= 330 and y >= 300 and y <= 400:
            organize()
            currentstate = menu
        # if the user were to press retry
        elif x >= 460 and x <= 590 and y >= 300 and y <= 400:
            organize()
            currentstate = play

    return currentstate


'''Main code:'''

import pygame
import random

pygame.init()

SIZE = (width, height) = (800, 500)
screen = pygame.display.set_mode(SIZE)

#colours
BBYBLUE = (190, 226, 230)
DRKBLUE = (157, 191, 196)
GREEN = (165, 247, 156)
BLACK = (0, 0, 0)
YT = (255, 255, 255)
RED = (255, 0, 0)
NEON = (193, 250, 102)

#clock, wll use later
myClock = pygame.time.Clock()

#setting up the images
backgroundPic = pygame.image.load("sky.png")
ewaste = pygame.image.load("e-waste.png")
catpic = pygame.image.load("cat.png")
flagpic = pygame.image.load("surrender flag.png")
livespic = pygame.image.load("cat2.png")
fullhealth = pygame.image.load("full health.png")
notfullhealth = pygame.image.load("points.png")

#scaling the images
backgroundPic = pygame.transform.scale(backgroundPic, (width, height))

catpic = pygame.transform.scale(
    catpic, (catpic.get_width() // 10, catpic.get_height() // 10))

ewaste = pygame.transform.scale(
    ewaste, (ewaste.get_width() // 20, ewaste.get_height() // 10))

flagpic = pygame.transform.scale(
    flagpic, (flagpic.get_width() // 10, flagpic.get_height() // 10))

livespic = pygame.transform.scale(
    livespic, (livespic.get_width() // 23, livespic.get_height() // 20))

#starting set up
x = y = my = mx = button = 0

#setting up the arrow keys
rightarrow = False
leftarrow = False

#states you can be in
menu = 0
play = 1
instruct = 2
instruct2 = 22
leaderboard = 3
createacc = 4
admin = 5
exit = 6
wait = 8
deathstate = -1

currentstate = menu

#playing shootings

shotTimer = pygame.time.get_ticks()  # time of last shot

missilestart = []  #y starting value of the bullets
bullets = []

enemy_xyvalue = initTarget()
enemyrect = pygame.Rect(enemy_xyvalue[0], enemy_xyvalue[1], 50, 5)
bulletrect = pygame.Rect(0, 0, 0, 0)

points = 0
addedpoints = 0

speed = 5

space = False

livesleft = 5

collision = False

#creating account
writingtextt = False
inputtext = ""
letter = ""
keyreturn = False
backspace = False
keydown = True

#starting positions of the cat
X = 400
Y = 400
scale = 0.5

#leaderboard
rankings = []
username = []
amtslayed = []

newrankings = []
newusername = []
newamtslayed = []

page = 0

#leaderboard variables
name = "Anonymous Cat"
inputtext = ""

openfile = open("leaderboard.dat", "r")

#reading the file and adding to list
while True:
    fields = openfile.readline()
    fields = fields.rstrip("\n")
    if fields == "":
        break
    data = fields.split(",")
    rankings.append(data[0])
    username.append(data[1])
    amtslayed.append(data[2])

#game loop starts
running = True

while running:
    button = 0

    for e in pygame.event.get():
        #finding the position of the mouse
        mx, my = pygame.mouse.get_pos()

        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            button = e.button

        elif e.type == pygame.MOUSEMOTION:
            mx, my = e.pos

        elif e.type == pygame.KEYDOWN:
            keydown = True
            letter = str(e.unicode)

            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                rightarrow = True

            elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                leftarrow = True

            elif e.key == pygame.K_SPACE or e.key == pygame.K_w or e.key == pygame.K_UP:
                space = True

            elif e.key == pygame.K_BACKSPACE:
                backspace = True

            elif e.key == pygame.K_RETURN:
                keyreturn = True

        elif e.type == pygame.KEYUP:
            keydown = False

            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                rightarrow = False

            elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                leftarrow = False

            elif e.key == pygame.K_SPACE or e.key == pygame.K_w or e.key == pygame.K_UP:
                space = False

            elif e.key == pygame.K_BACKSPACE:
                backspace = False

            elif e.key == pygame.K_RETURN:
                keyreturn = False
    #main menu
    if currentstate == menu:
        currentstate = drawMENU(screen, currentstate, x, y, mx, my, button)

    #play menu
    elif currentstate == play:
        moving(screen, currentstate, button, X, Y, scale)
        enemyrect = drawEnemies(screen, enemy_xyvalue)
        bulletrect = shooting(screen, button, X, Y, collision)

        #if the amount of lives become 0
        if livesleft == 0:
            currentstate = deathstate
            screen.blit(backgroundPic, (0, 0, 800, 500))
            pointts = "Score: " + str(points)
            pywritetext((30, 30, 100, 10), BLACK, pointts, 20)
            screen.blit(catpic, (X, Y))
            screen.blit(flagpic, (700, 0, 100, 100))

        #if the user were to surrender
        if button == 1:
            if x >= 700 and x <= 800 and y >= 0 and y <= 100:
                currentstate = deathstate
                screen.blit(backgroundPic, (0, 0, 800, 500))
                pointts = "Score: " + str(points)
                pywritetext((30, 30, 100, 10), BLACK, pointts, 20)
                screen.blit(catpic, (X, Y))
                screen.blit(flagpic, (700, 0, 100, 100))
    elif currentstate == wait:
        currentstate = drawWAIT(screen, currentstate, button, x, y)
    #when the user dies
    elif currentstate == deathstate:
        organize()
        writeinfo()

        #restarting the values for the next user
        enemy_xyvalue = initTarget()
        currentstate = drawDEATH(screen, currentstate, button, x, y)
        bullets = []
        missilestart = []
        livesleft = 5
        points = 0
        addedpoints = 0
        speed = 5
        X = 400
        Y = 400

    #first page of instructions
    elif currentstate == instruct:
        currentstate = drawINSTRUCTIONS(screen, currentstate, x, y, button)
    #second page of instructions
    elif currentstate == instruct2:
        currentstate = drawINSTRUCTIONS2(screen, currentstate, x, y, button)
    #page for leaderboard
    elif currentstate == leaderboard:
        currentstate = drawLEADERBOARD(screen, currentstate, x, y)

    #page for creating account
    elif currentstate == createacc:
        name = drawCREATEACC(screen, currentstate, x, y, button)

        #ways to return to the menu
        if button == 1:
            if x >= 730 and x <= 800 and y >= 0 and y <= 70:
                currentstate = menu
        if keyreturn == True:
            currentstate = menu
    #exiting
    elif currentstate == exit:
        running = False

    pygame.display.flip()

    myClock.tick(60)


pygame.quit()