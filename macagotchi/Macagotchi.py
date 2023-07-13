#License:
#MIT License
#Copyright SpaceMonkeyAlfa 2023
import time
import subprocess
import datetime
from datetime import datetime as datetime2
import pygame
import random
import hashlib
import asyncio
import sys

#handy code-snippet to manage file directories no matter which directory you run macagotchi in
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
pygame.init()
#Define Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
colour = (184, 230, 229)
GREEN = (0,255,0)
RED = (255,0,0)
#Open Window
width = 350
height = 125
size = (width, height)
img = pygame.transform.scale(pygame.image.load('assets/logo.png'),(160,100))
pygame.display.set_icon(img)
screen = pygame.display.set_mode(size)
addup = 0
streak = 0
commentary = ""
uniques = []
scanning = False
textColour = WHITE
pygame.display.set_caption("Macagotchi")
typing = False
displayResults = False
scanDelay = 0
with open('assets/address.txt','r') as f:
        file = f.read()
        values = file.split('\n')
        ssids = len(values)
with open('assets/longestStreak.txt','r') as f:
    file = f.read()
    longestStreak = int(file.split('\n')[0])
with open('assets/stats.txt','r') as f:
    file = f.read()
    nameText = file.split('\n')[0]
#Streak manager
with open('assets/loyalty.txt','r') as f:
    file = f.read()
    values = file.split('\n')
    for d in values:
        if d != "":
            streak += 1
    if str(datetime.date.today()-datetime.timedelta(days=1)) not in values and str(datetime.date.today()) not in values:
       print("STREAK BROKEN!")
       print(str(datetime.date.today()))
       with open('loyalty.txt','w') as f:
         f.write("")
         streak = 0
with open('assets/totalLog.txt','r') as f:
    file = f.read()
    file = file.split('\n')
    
    file = file[len(file)-1]
    print(file)
    file = file.split(',')
    if "".join(file) != "":
        lastopened = file[1]
        str_d1 = str(datetime.date.today())
        str_d2 = lastopened
        d1 = datetime2.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime2.strptime(str_d2, "%Y-%m-%d")

        sleepTime = d1 - d2
        sleepTime = sleepTime.days
    else:
        sleepTime = 0

def ezhash(string):
    hasher = hashlib.sha256()
    hasher.update(string.encode('utf8'))
    return hasher.hexdigest()
            
process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
def scan(count):
    ct = datetime.datetime.now()
    ts = ct.timestamp()
    process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    networks = out.decode().split('\n')

    networks.pop(0)
    netwrks = []
    for n in networks:
        count = 0
        n = n.split('--')
        n = str(n[0]).split()
        if len(n) > 0:
            i = 0
            while i < len(n) - 4:
                n[0] += " "+n[i+1]
                i += 1
            netwrks.append(n[0])
        else:
            continue

        networks = netwrks
    for n in networks:
        with open('assets/address.txt','r') as f:
            file = f.read()
            values = file.split('\n')
            ssids = len(values)   
        if ezhash(n) not in values:
            with open('assets/address.txt','a') as f:
                f.write('\n'+str(ezhash(n)))
                count += 1
                if n != "":
                    uniques.append(n)
                print(n)
            
        with open('assets/totalLog.txt','a') as f:
                f.write('\n'+str(ezhash(n)))
                f.write(','+str(datetime.date.today()))
    return(count)


screen.fill(WHITE)
pygame.display.flip()
carryOn = True
timer = 1400
clock = pygame.time.Clock()
count = 0
happy = pygame.transform.scale(pygame.image.load('assets/awake.jpg'),(150,90))
scanning1 = pygame.transform.scale(pygame.image.load('assets/scanning1.jpg'),(150,90))
scanning2 = pygame.transform.scale(pygame.image.load('assets/scanning2.jpg'),(150,90))
scanning3 = pygame.transform.scale(pygame.image.load('assets/scanning3.jpg'),(150,90))
friendly = pygame.transform.scale(pygame.image.load('assets/friendly.jpg'),(150,90))
normal = pygame.transform.scale(pygame.image.load('assets/happy.jpg'),(150,90))
bored = pygame.transform.scale(pygame.image.load('assets/bored.jpg'),(150,90))
lonely = pygame.transform.scale(pygame.image.load('assets/lonely.jpg'),(150,90))
blink = pygame.transform.scale(pygame.image.load('assets/blink.jpg'),(150,90))
low = pygame.transform.scale(pygame.image.load('assets/0-9.jpg'),(300,100))
medium = pygame.transform.scale(pygame.image.load('assets/10-29.jpg'),(300,100))
high = pygame.transform.scale(pygame.image.load('assets/30-99.jpg'),(300,100))
godtier = pygame.transform.scale(pygame.image.load('assets/100+.jpg'),(300,100))
asleep = pygame.transform.scale(pygame.image.load('assets/asleep.jpg'),(150,90))
awakening = pygame.transform.scale(pygame.image.load('assets/awakening.jpg'),(150,90))
face = asleep
nextface = normal
oldface = normal
finds = 0
actualTime = 0
scanTimes = 0
scanning = False
blinkTime = 0
networksID = 0
displayTime = 0
lastFinds = 0
while carryOn:
    screen.fill(WHITE)
    for event in pygame.event.get():
    #time.sleep(1)
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_F2:
                typing = True
            if event.key == pygame.K_RETURN:
                typing = False
                with open('assets/stats.txt','w') as f:
                    f.write(nameText)

                
            elif event.key == pygame.K_BACKSPACE and typing:
                # get text input from 0 to -1 i.e. end.
                nameText = nameText[:-1]
  
            # Unicode standard is used for string
            # formation
            elif typing and len(nameText) < 11:
                nameText += event.unicode
    if actualTime == 60:
        face = awakening
        sleepTime = sleepTime
        if sleepTime == 1:
            commentary = f"I've been asleep for {sleepTime} day."
        elif sleepTime > 1:
            commentary = f"I've been asleep for {sleepTime} days."
        else:
            commentary = "Hello hooman!"
            
    if actualTime == 120:
        face = normal
  
    
        
    if timer == 1800+scanDelay:
        displayResults = False
        if longestStreak < streak:
            with open('assets/longestStreak.txt','w') as f:
                f.write(str(streak))
        rng = random.randint(1,4)
        commentary = "Scanning..."
        print("Scanning...")
        scanning = True
        uniques = []
        lastFinds = scan(0)
        face = scanning1
        finds += lastFinds
    if timer in range(1845+scanDelay,1850+scanDelay):
        face = scanning2
    elif timer in range(1890+scanDelay,1895+scanDelay):
        face = scanning3
    elif timer in range(1935+scanDelay,1940+scanDelay):
        face = scanning2
    elif timer in range(1980+scanDelay,1985+scanDelay):
        face = scanning1
    elif timer in range(2025+scanDelay,2030+scanDelay):
        face = scanning2
    elif timer in range(2070+scanDelay,2075+scanDelay):
        face = scanning3
    elif timer in range(2115+scanDelay,2120+scanDelay):
        face = scanning2
    elif timer >= 2205:
        scanning = False
        timer = 0
        face = nextface
        displayResults = True
        networksID = 0
        with open('assets/address.txt','r') as f:
            file = f.read()
            values = file.split('\n')
            ssids = len(values)
        scanTimes += 1
        if lastFinds < 1 and not scanning:
            commentary = "Found nothing."


    if lastFinds > 0 and displayResults:
        timer = 0
        commentary = f"Found {uniques[networksID]}!"
        displayTime += 1
        if displayTime > 60 and networksID < len(uniques)-1:
            networksID += 1
            displayTime = 0
        elif displayTime > 60:
            if lastFinds > 1:
                commentary = f"Found {lastFinds} new ones!"
            elif lastFinds == 1:
                commentary = f"Found {lastFinds} new one!"       
            displayTime = 0
            displayResults = False

    if finds > 4 and not scanning:
        face = friendly
        nextface = friendly
        with open('assets/loyalty.txt','r') as f:
            file = f.read()
            values = file.split('\n')
        if str(datetime.date.today()) not in values:
            with open('assets/loyalty.txt','a') as f:
                f.write('\n'+str(datetime.date.today()))
                streak += 1
    elif finds > 0 and not scanning:
        face = happy
        nextface = happy
    elif finds < 1 and scanTimes > 0 and not scanning:
        face = lonely
        nextface = lonely


        if rng == 1:
            commentary = "Hungry"
        elif rng == 2:
            commentary = "Feed.. Me"
        elif rng == 3:
            commentary = "Food.."
        elif rng == 4:
            commentary = "Can we go for a walk?"


    
    blinkTime += 1
    if blinkTime == 180 and not scanning and face != lonely:
        oldface = face
    if blinkTime > 180 and not scanning and face != lonely:
        face = blink
    if blinkTime > 195 and not scanning and face != lonely:
        face = oldface
        blinkTime = 0
    with open('assets/totalLog.txt','r') as f:
        file = f.read()
        total = len(file.split('\n'))
    if len(str(streak)) > 1:
        adjustmentX = 6
    if len(str(streak)) > 2:
        adjustmentX = 12
    if len(str(streak)) < 2:
        adjustmentX = 0

    message = str(streak)
    font = pygame.font.SysFont('Menlo', 20)
    text_surface = font.render(message, False, textColour)
    commentaryText = font.render(commentary, False, BLACK)
    name = font.render(str(nameText), False, (0, 0, 0))
    #ssidText = font.render(str(ssids-1), False, (0, 0, 0))
    ssidText = font.render(str(ssids-1), False, (0, 0, 0))
    countText = font.render(str(total+addup-1), False, (0, 0, 0))
    if longestStreak < 10:
        screen.blit(low, (25,10))
    elif longestStreak < 30:
        screen.blit(medium, (25,10))
    elif longestStreak <= 100:
        screen.blit(high, (25,10))
    elif longestStreak > 100:
        screen.blit(godtier, (25,10))
        textColour = (245, 227, 66)
    screen.blit(face,(0, 20))
    screen.blit(commentaryText,(20, 100) )
   
   
    screen.blit(ssidText, (230,40))
    screen.blit(countText, (230,60))
    screen.blit(text_surface, (176-adjustmentX,50))

    screen.blit(name, (10, 10))
    timer+=1
    actualTime += 1

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
    
    
