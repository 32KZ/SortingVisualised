##Imports
import turtle
import random
import time

##Main

##Variables
turtle.speed(10000)
numlist = []
rainbow =["violet","pink","indigo"]

##


# until our list is length 50,
# add a random number from 0-150 thats not already in list.

while len(numlist) != 50:
  num = random.randint(0,150)
  if num not in numlist:    
    numlist.append(num)

##
#Position Turtle
turtle.left(90)
turtle.penup()
turtle.goto(-200,0)
turtle.width(10)
turtle.pendown()


def drawgraph(rainbow,numlist):
  for num in numlist:
    position = turtle.pos() #Save Position of turtle in X and Y as [0],[1]

    turtle.color("white") #Clear the collumn
    turtle.forward(200)

    turtle.goto(position[0],position[1]) #Go to base of Column

    turtle.color(rainbow[random.randint(0,(len(rainbow))-1)])
    #Our turtle Color is the index of a color in Rainbow of a random number
    #that does not excede the length of rainbow.
    
    turtle.forward(num) #Draw the Number.
    turtle.goto(position[0],position[1])#goto Base of Column

    #realign the turtle 10PX to the right.
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

    #Changes:
    # Make a Better Random Selector. (random(rainbow))
    # make the repositioning after column drawn more efficient with Goto
    # possibly save positions of Num with Pos in a dictionary.

drawgraph(rainbow,numlist)
#Draw Graph initailly.


##Start of Bubble Sort

swaps = 1
passes = 0
while swaps != 0:
  swaps = 0
  for num in numlist:
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()

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
    if passes % 200 == 0: # refresh rate. every 200 passes.
      drawgraph(rainbow,numlist)
     
print(numlist)
print(passes)
drawgraph(rainbow,numlist)
