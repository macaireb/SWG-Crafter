from tkinter import *
import craft
import importlib

root = Tk()
root.minsize(550, 275)
root.title("SWGCraft - MacaireBell.com")


stageLab = [(Label(root, text='Stage {} X,Y'.format(i))) for i in range(1, 6)]
stageLocX, stageLocY = [(Entry(root)) for i in range(5)], [(Entry(root)) for i in range(5)]
toolLab = [Label(root, text='Tool {} X,Y'.format(i)) for i in range(1, 6)] #add option to reduce tool count later
toolX, toolY = [(Entry(root)) for i in range(5)],  [(Entry(root)) for i in range(5)]
resLab = [Label(root, text='Resource {} X,Y'.format(i)) for i in range(1, 6)] #add option to reduce tool count later
resX, resY = [(Entry(root)) for i in range(5)],  [(Entry(root)) for i in range(5)]
itemLabel = Label(root, text='Location of the item')
itemLocX, itemLocY = Entry(root), Entry(root)
loopLab = Label(root, text='How Many loops? *Caution*')
loop = Entry(root)
delayLab = Label(root, text='Seconds delay per stage')
delay = Entry(root)
[i.place(relx=0, rely=.1*(stageLab.index(i)), relheight=.1, relwidth=.1) for i in stageLab]
[i.place(relx=.1, rely=.1*(stageLocX.index(i)), relheight=.1, relwidth=.05) for i in stageLocX]
[i.place(relx=.15, rely=.1*(stageLocY.index(i)), relheight=.1, relwidth=.05) for i in stageLocY]
[i.place(relx=.25, rely=.1*(toolLab.index(i)), relheight=.1, relwidth=.1) for i in toolLab]
[i.place(relx=.35, rely=.1*(toolX.index(i)), relheight=.1, relwidth=.05) for i in toolX]
[i.place(relx=.4, rely=.1*(toolY.index(i)), relheight=.1, relwidth=.05) for i in toolY]
[i.place(relx=.45, rely=.1*(resLab.index(i)), relheight=.1, relwidth=.15) for i in resLab]
[i.place(relx=.6, rely=.1*(resX.index(i)), relheight=.1, relwidth=.05) for i in resX]
[i.place(relx=.65, rely=.1*(resY.index(i)), relheight=.1, relwidth=.05) for i in resY]
loopLab.place(relx=.25, rely=.55, relheight=.1, relwidth=.3)
loop.place(relx=.55, rely=.55, relheight=.1, relwidth=.05)
delayLab.place(relx=.25, rely=.65, relheight=.1, relwidth=.3)
delay.place(relx=.55, rely=.65, relheight=.1, relwidth=.05)
itemLabel.place(relx=.25, rely=.8, relheight=.1, relwidth=.25)
itemLocX.place(relx=.5, rely=.8, relheight=.1, relwidth=.05)
itemLocY.place(relx=.55, rely=.8, relheight=.1, relwidth=.05)


def loadLayout():
    craft.loadLayout()
    [toolX[craft.tools.index(i)].insert(END, i[0]) for i in craft.tools]
    [toolY[craft.tools.index(i)].insert(END, i[1]) for i in craft.tools]
    [resX[craft.resources.index(i)].insert(END, i[0]) for i in craft.resources]
    [resY[craft.resources.index(i)].insert(END, i[1]) for i in craft.resources]
    [stageLocX[craft.stages.index(i)].insert(END, i[0]) for i in craft.stages]
    [stageLocY[craft.stages.index(i)].insert(END, i[1]) for i in craft.stages]


def startCrafting():
    craft.toolX = [int(toolX[i].get()) for i in range(len(toolX)) if (toolX[i].get() is not '')]
    craft.toolY = [int(toolY[i].get()) for i in range(len(toolY)) if (toolY[i].get() is not '')]
    craft.resX = [int(resX[i].get()) for i in range(len(resX)) if resX[i].get() is not '']
    craft.resY = [int(resY[i].get()) for i in range(len(resY)) if resY[i].get() is not '']
    craft.stagesX = [int(stageLocX[i].get()) for i in range(len(stageLocX)) if stageLocX[i].get() is not '']
    craft.stagesY = [int(stageLocY[i].get()) for i in range(len(stageLocY)) if stageLocY[i].get() is not '']
    if itemLocX.get() is not '' and itemLocY.get() is not '':
        craft.item = (int(itemLocX.get()), int(itemLocY.get()))
    if loop.get() is not '':
        craft.loop = int(loop.get())
    print(craft.loop)
    craft.tools = craft.setTools()
    craft.stages = craft.setStages()
    craft.resources = craft.setResources()
    craft.outputLoad()
    craft.saveLayout()
    craft.craft()
    importlib.reload(craft)


run = Button(text='Start Crafting', command=lambda: startCrafting())
run.place(relx=.75, rely= .2, relheight=.1, relwidth=.2)
try:
    open("layout.txt", "r")
except FileNotFoundError:
    open("layout.txt", "w")
loadLayout()
root.mainloop()
