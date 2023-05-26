##Original Code By Victoria Miller aka Juuls
##Edits Made By 32KZ

##Imports
import turtle
import random
import time

##Main

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


def resetTurtle():
  turtle.reset()
  turtle.setworldcoordinates(-400, -400, 400, 400)
  turtle.left(90) # turtle by defualt faces East.
  turtle.penup()
  turtle.goto(-380,-320)
  turtle.width(10)

def drawgraph(rainbow,numlist):
  turtle.goto(-380,-320)
  for num in numlist:
    #realign the turtle 10PX to the right.
    myxpos = turtle.xcor()
    turtle.setx(myxpos + 15)
    position = turtle.pos() #Save Position of turtle in X and Y as [0],[1]
    
    turtle.pd()
    turtle.color("white") #Clear the collumn
    turtle.forward(151)
    turtle.goto(position[0],position[1]) #Go to base of Column
    turtle.penup()
    
    turtle.color(rainbow[random.randint(0,(len(rainbow))-1)])
    #Our turtle Color is the index of a color in Rainbow of a random number
    #that does not excede the length of rainbow.
    turtle.pendown()
    turtle.forward(num) #Draw the Number.
    turtle.goto(position[0],position[1])#goto Base of Column
    turtle.penup()
    
resetTurtle()
drawgraph(rainbow,numlist)
#Draw Graph initailly.


##Start of Bubble Sort

swaps = 1
passes = 0
while swaps != 0:
  swaps = 0
  for num in numlist:



    try:
      num1 = numlist[numlist.index(num)]
      num2 = numlist[numlist.index(num)+ 1]
    except IndexError:
      break
    if num1 > num2:
      numlist[numlist.index(num2)] = num1
      numlist[numlist.index(num1)] = num2
      swaps += 1

    passes += 1
    if passes % 150 == 0: # refresh rate. 
      drawgraph(rainbow,numlist)
    if passes % 300 == 0:
      resetTurtle()
      
     
print(numlist)
print(passes)
resetTurtle()
drawgraph(rainbow,numlist)
