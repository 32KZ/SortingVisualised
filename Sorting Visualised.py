##Original Code By Victoria Miller aka Juuls
##Edits Made By 32KZ

##Imports
import turtle
import random
import time


##Variables
turtle.speed(0)
turtle.delay(0)
numlist = []
rainbow =["violet","pink","indigo"]

##


# until our list is length 50,
# add a random number from 0-150 thats not already in list.

while len(numlist) != 50:
  num = random.randint(0,150)
  if num not in numlist:    
    numlist.append(num)

##Set View
turtle.setworldcoordinates(-400, -400, 400, 400)


def resetTurtle():
  turtle.reset()
  turtle.setworldcoordinates(-400, -400, 400, 400)
  turtle.left(90) # turtle by defualt faces East.
  turtle.penup()
  turtle.goto(-380,-320)
  turtle.width(10)

def drawgraph(numlist , CellPositions):
    x = 0
    turtle.goto(-380,-320)
    for num in numlist:

        #realign the turtle 10PX to the right.
        myxpos = turtle.xcor()
        turtle.setx(myxpos + 15)
        CellPositions[x] = turtle.xcor() # assign index an Xcor
        x = x+1 #increment x
        
        position = turtle.pos() #Save Position of turtle in X and Y as [0],[1]
    
        turtle.pd()
        turtle.color("white") #Clear the collumn
        turtle.forward(151)
        turtle.penup()
    
        turtle.goto(position[0],position[1]) #Go to base of Column
        turtle.color("red")
        turtle.pendown()
        turtle.forward(num) #Draw the Number.
        turtle.goto(position[0],position[1])#goto Base of Column
        turtle.penup()
    turtle.goto(-380,-320)
    return CellPositions


def ClearGraph(CellPos):
    turtle.color("white")
    for index in CellPos:
      newXPos = CellPos[index]
      turtle.goto(newXPos,-320)
      turtle.pd()
      turtle.fd(151)
      turtle.up()
      turtle.bk(151)
    #turtle.goto(-360,-320)
###SUMMARY OF CLEARGRAPH
#Instead of just reseting the turtle we need to make a change,
#the ClearGraph Function allows us to select all the changed cells,
#    (dictated by its dict input)
# and clear them.
# we do not need to go to start at the end, since that is resetTurtle()'s job.
#this means that we can call this on a given range of indexes through a
#dict structure, and it will wipe them for us to Draw.
# with regards to Memory, the process for this is as follows.
# Clear range > draw new data after sort > next itteration we refresh turtle.
# this is mostly asetetic, but it feels nicer than just a reset.
###

def quicksort(numlist):
    if len(numlist) == 1:
        return numlist
    else:
        pivot = len(numlist) // 2 
        pivot = numlist[pivot]
        #sort the data list
        smaller = [x for x in numlist < pivot]
        equal = [x for x in numlist == pivot]
        bigger = [x for x in numlist > pivot]
        
        #render it in a flashy way with new function

        
        return quicksort(smaller) + pivot + quicksort(bigger)

  

##Main

resetTurtle()

cellPositionsDict = {
    -1 : -380,
    0  : -365
    }

cellPositionsDict = drawgraph(numlist , cellPositionsDict)

print(cellPositionsDict)

ClearGraph(cellPositionsDict)
resetTurtle()

cellPositionsDict = drawgraph(numlist , cellPositionsDict)
#sorted_array = quicksort(numlist)
#print(sorted_array)
    
