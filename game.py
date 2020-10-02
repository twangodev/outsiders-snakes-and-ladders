import pygame
import json
import time
import random
import datetime

with open('config.json') as configuration: #Read JSON from config.json
    config = json.loads(configuration.read())

#Initialize pygame
pygame.init()

# Create Window
gameDisplay = pygame.display.set_mode((config["display"]["width"], config["display"]["height"]))
pygame.display.set_caption(config["display"]["caption"])

#Load Images
startingbg = pygame.image.load("./assets/startingbg.png")
startbtn = pygame.image.load("./assets/startbtn.png")
grid = pygame.image.load("./assets/grid.png")
snake = pygame.image.load("./assets/snake.png")
banner = pygame.image.load("./assets/announcement.png")
checkmark = pygame.image.load("./assets/check.png")
xmark = pygame.image.load("./assets/xmark.png")
continuebtn = pygame.image.load("./assets/continue.png")
quitbtn = pygame.image.load("./assets/quit.png")

dice = [pygame.image.load("./assets/dice/1.png"), pygame.image.load("./assets/dice/2.png"), pygame.image.load("./assets/dice/3.png"), pygame.image.load("./assets/dice/4.png"), pygame.image.load("./assets/dice/5.png"), pygame.image.load("./assets/dice/6.png")]

#Variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def centercoord(imageh, imagew):
    centerscreencoord_height = config["display"]["height"]
    centerscreencoord_width = config["display"]["width"]
    x = (centerscreencoord_width/2)-(imagew/2)
    y = (centerscreencoord_height/2)-(imageh/2)
    return [int(x),int(y)]

def move(offset):
    x, y = offset
    x += 60
    if x > 650:
        x = config["snake-xoffset"]
        if y != 540:
            y += 60
        else:
            print("You win")
    return [x, y]

def offset_to_pos(offset):
    x, y = offset
    x -= config["snake-xoffset"]
    pos_x = x/60
    pos_y = y/60
    return [int(pos_x), int(pos_y)]

def correct_checker(id, ug_answer):
    id = str(id)
    answer = config["answers"][id]
    if type(answer) == list:
        for each_answer in answer:
            if each_answer.lower() == str(ug_answer).lower():
                return True
        return False
    elif type(answer) == str:
        if ug_answer.lower() == answer.lower():
            return True
        else:
            return False

#Main Modules

def start():
    gameDisplay.fill([42, 42, 42])
    loop = True
    while(loop == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                print("Game Quit")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= centercoord(30,100)[0] and event.pos[0] <= (centercoord(30,100)[0]+100) and event.pos[1] >= centercoord(30,100)[1] and event.pos[1] <= (centercoord(30,100)[1]+30):
                    mainscreen()
                    loop = False
        gameDisplay.blit(startingbg, [0,0]) #Set Background
        gameDisplay.blit(startbtn, centercoord(30, 100))
        pygame.display.update()
        clock.tick(config["display"]["fps"])
        pygame.display.flip()

def mainscreen():
    id_randomized = []
    for x in config["questions"].keys():
        id_randomized.append(x)
    random.shuffle(id_randomized)
    print("Question Order: {}".format(id_randomized))

    #Private Variables
    start_time = datetime.datetime.now()
    answer = "" 
    provided_answer = ""
    offset = [config["snake-xoffset"], 0]
    position = [0,0]
    loop = True
    diceface = dice[0]
    displaycube = False
    bannerdisplay = False
    answer_text = ""
    stoprolling = True
    collectbannerbuttons = False
    while(loop == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                print("Game Quit")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                elif event.key == pygame.K_RETURN:
                    provided_answer = answer
                    answer = ""
                    bannerdisplay = True
                    stoprolling = False
                else:
                    letter = str(keystroke_recorder(event))
                    answer = answer + letter #Adding Letters
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if collectbannerbuttons == True:
                    if event.pos[0] >= int(config["display"]["width"]/2-180) and event.pos[0] <= int((config["display"]["width"]/2-180)+100) and event.pos[1] >= int(config["display"]["height"]/2+40) and event.pos[1] <= int((config["display"]["height"]/2+40)+30):
                        loop = False
                    if event.pos[0] >= int(config["display"]["width"]/2-50) and event.pos[0] <= int(int(config["display"]["width"]/2-50)+200) and event.pos[1] >= int(config["display"]["height"]/2+10) and event.pos[1] <= int(int(config["display"]["height"]/2+40)+30):
                        bannerdisplay = False
                        id_randomized.pop(0)
        #Display
        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(grid, [0,0]) #Set Background
        #Score Update
        score = str(position[0] + (position[1]*10) + 1)
        score_text = font.render("Score: " + score, True, (0,0,0), (255,255,255))
        gameDisplay.blit(score_text, [0,0])
        #Time
        time_elapsed = str(round((datetime.datetime.now() - start_time).total_seconds()))
        time_text = font.render("Seconds Elapsed: " + time_elapsed, True, (0,0,0), (255,255,255))
        gameDisplay.blit(time_text, [0, config["display"]["height"]-20])
        #Snake
        gameDisplay.blit(snake, offset)
        #Question
        try:
            question = config["questions"][id_randomized[0]]
        except Exception:
            print("Out of questions.")
            loop = False
        question_text = font.render("Question: " + question, True, (0,0,0), (255,255,255))
        gameDisplay.blit(question_text, [0, config["display"]["height"]-40])
        #Answer Text Update
        answer_text = font.render("Your Answer: " + str(answer), True, (0,0,0), (255,255,255)) #Answer
        gameDisplay.blit(answer_text, [int((config["display"]["width"]/2)-200), int(config["display"]["height"]-20)])
        #Announcments
        if bannerdisplay == True:
            provided_answer_text = font.render("Your Answer: " + provided_answer, True, (0,0,0))
            gameDisplay.blit(banner, centercoord(341, 604))
            gameDisplay.blit(provided_answer_text, [int(config["display"]["width"]/2-180), int(config["display"]["height"]/2-75)])
            if correct_checker(id_randomized[0], provided_answer) == True:
                gameDisplay.blit(checkmark, [int(config["display"]["width"]/2), int(config["display"]["height"]/2-70)])
                #If Correct Move the Snake
                displaycube = True
                if stoprolling == False:
                    randomnumber = random.randint(1,6)
                    diceface = dice[randomnumber-1]
                    print("Random Number: " + str(randomnumber))
                    for x in range(randomnumber):
                        offset = move(offset)
                        position = offset_to_pos(offset)
                    stoprolling = True
                rolled_text = font.render("You rolled a " + str(randomnumber), True, (0,0,0)) #Rolled Text
                gameDisplay.blit(rolled_text, [int(config["display"]["width"]/2-180), int(config["display"]["height"]/2-30)])
                #Render Buttons
                collectbannerbuttons = True
                gameDisplay.blit(quitbtn, [int(config["display"]["width"]/2-180), int(config["display"]["height"]/2+40)])
                gameDisplay.blit(continuebtn, [int(config["display"]["width"]/2-80), int(config["display"]["height"]/2+40)])
            elif correct_checker(id_randomized[0], provided_answer) == False:
                gameDisplay.blit(xmark, [int(config["display"]["width"]/2-180), int(config["display"]["height"]/2-50)])
                displaycube = False
                #Render Buttons
                collectbannerbuttons = True
                gameDisplay.blit(quitbtn, [int(config["display"]["width"]/2-180), int(config["display"]["height"]/2+40)])
                gameDisplay.blit(continuebtn, [int(config["display"]["width"]/2-50), int(config["display"]["height"]/2+40)])
        else:
            collectbannerbuttons = False
        if displaycube == True:
            previous_roll_text = font.render("Previous Roll:", True, (0,0,0))
            gameDisplay.blit(previous_roll_text, [0, 40])
            gameDisplay.blit(diceface, [0, 60])
        clock.tick(config["display"]["fps"])
        pygame.display.update()
        pygame.display.flip()

def keystroke_recorder(event):
    if event.type == pygame.KEYDOWN:
        #Alpha Keys
        if event.key == pygame.K_q:
            return "q"
        elif event.key == pygame.K_w:
            return "w"
        elif event.key == pygame.K_e:
            return "e"
        elif event.key == pygame.K_r:
            return "r"
        elif event.key == pygame.K_t:
            return "t"
        elif event.key == pygame.K_y:
            return "y"
        elif event.key == pygame.K_u:
            return "u"
        elif event.key == pygame.K_i:
            return "i"
        elif event.key == pygame.K_o:
            return "o"
        elif event.key == pygame.K_p:
            return "p"
        elif event.key == pygame.K_a:
            return "a"
        elif event.key == pygame.K_s:
            return "s"
        elif event.key == pygame.K_d:
            return "d"
        elif event.key == pygame.K_f:
            return "f"
        elif event.key == pygame.K_g:
            return "g"
        elif event.key == pygame.K_h:
            return "h"
        elif event.key == pygame.K_j:
            return "j"
        elif event.key == pygame.K_k:
            return "k"
        elif event.key == pygame.K_l:
            return "l"
        elif event.key == pygame.K_QUOTE:
            return "'"
        elif event.key == pygame.K_z:
            return "z"
        elif event.key == pygame.K_x:
            return "x"
        elif event.key == pygame.K_c:
            return "c"
        elif event.key == pygame.K_v:
            return "v"
        elif event.key == pygame.K_b:
            return "b"
        elif event.key == pygame.K_n:
            return "n"
        elif event.key == pygame.K_m:
            return "m"
        #Number Keys
        elif event.key == pygame.K_1:
            return "1"
        elif event.key == pygame.K_2:
            return "2"
        elif event.key == pygame.K_3:
            return "3"
        elif event.key == pygame.K_4:
            return "4"
        elif event.key == pygame.K_5:
            return "5"
        elif event.key == pygame.K_6:
            return "6"
        elif event.key == pygame.K_7:
            return "7"
        elif event.key == pygame.K_8:
            return "8"
        elif event.key == pygame.K_9:
            return "9"
        elif event.key == pygame.K_0:
            return "0"
        #Space
        elif event.key == pygame.K_SPACE:
            return " "
        else:
            return ""

start()