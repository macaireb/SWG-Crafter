import time, pyautogui

def click():
    pyautogui.mouseDown()
    time.sleep(d)
    pyautogui.mouseUp()

def LoadResource(coord):
    #add check for blank gui
    pyautogui.moveTo(coord[0], coord[1])
    time.sleep(d)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def NextStage(coord):
    if coord[0] or coord[1] is not '': #check if parameter from GUI is blank
        pyautogui.moveTo(coord[0], coord[1])
        time.sleep(d)
        click()


tools = [] #((850, 695),(890, 695),(930, 695), (970, 695))#PRECU#((485, 20),(515, 20), (545, 20), (575,20))
item = (300, 625)#PRECU#(300, 625)
stages = [] #((820, 660),(1100, 630),(682, 615),(772, 606))#PRECU#((800, 655), (1100, 660), (680, 600), (760, 600))
resources = [] #((210, 210),(210, 210),(210, 210),(210, 210))#PRECU#((335, 215), (280, 215)) #, (335, 215))
ngeSample = (295, 480)
d = .1 #delay
dt = 2 #delay #2
loop = 1

toolX, toolY = [], []
itemX, itemY = None, None
stagesX, stagesY = [], []
resX, resY = [], []

def saveLayout():
    fLayOut = open('layout.txt', 'w')
    if(len(tools)):
        fLayOut.write('*tools* ')
        [fLayOut.write(str(t[0]) + ',' + str(t[1]) + ';') for t in tools]
        fLayOut.write('\n')
    if(len(resources)):
        fLayOut.write('*resources* ')
        [fLayOut.write(str(r[0]) + ',' + str(r[1]) + ';') for r in resources]
        fLayOut.write('\n')
    if(len(stages)):
        fLayOut.write('*stages* ')
        [fLayOut.write(str(s[0]) + ',' + str(s[1]) + ';') for s in stages]
        fLayOut.write('\n')
    fLayOut.close()


def loadLayout():
    lines = open('layout.txt', 'r').readlines()
    global tools, resources, stages
    for line in lines:
        print(line)
        if(line.split()[0] == '*tools*'):
            line = line.replace('*tools*', '').replace('\n', '')[:-1]
            print('tessir')
            tools = [(int(i.strip().split(',')[0]), int(i.split(',')[1])) for i in line.split(';')]
        if(line.split()[0] == '*resources*'):
            line = line.replace('*resources*', '').replace('\n', '')[:-1]
            print("ressir")
            resources = [(int(i.strip().split(',')[0]), int(i.split(',')[1])) for i in line.split(';')]
        if(line.split()[0] == '*stages*'):
            line = line.replace('*stages*', '').replace('\n', '')[:-1]
            print("sessir")
            stages = [(int(i.strip().split(',')[0]), int(i.split(',')[1])) for i in line.split(';')]

    [print(i) for i in tools]
    [print(i) for i in stages]
    [print(i) for i in resources]

def setTools():
    return [(toolX[i], toolY[i]) for i in range(min(len(toolX), len(toolY)))]

def setStages():
    return [(stagesX[i], stagesY[i]) for i in range(min(len(stagesX), len(stagesY)))]

def setResources():
    return [(resX[i], resY[i]) for i in range(min(len(resX), len(resY)))]

def setItem():
    item = (itemX, itemY)

def setFromGUI():
    setTools(); setStages(); setResources(); setItem()

def outputLoad():
    print("Tools")
    [print(i) for i in tools]
    print("Resources")
    [print(i) for i in resources]
    print("stages")
    [print(i) for i in stages]
    print("Item")
    print(item)


def craft():
    for counter in range(loop):
        time.sleep(dt)
        for j in tools:
            NextStage(j)
            time.sleep(dt)
            #NextStage(item)
            #time.sleep(dt)
            NextStage(stages[0])
            time.sleep(dt)
            for i in resources:
                LoadResource(i)
            time.sleep(dt)
            for i in stages[1:]:
                NextStage(i)
                time.sleep(dt)
