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
turtle.goto(-250,0)
turtle.width(10)
turtle.pendown()


def refreshGraph(numlist):
  for num in numlist:
    #realign the turtle 10PX to the right.
    myxpos = turtle.xcor()
    turtle.setx(myxpos + 10)
    position = turtle.pos() #Save Position of turtle in X and Y as [0],[1]
    
    turtle.pd()
    turtle.color("white") #Clear the collumn
    turtle.forward(151)
    turtle.goto(position[0],position[1]) #Go to base of Column
    turtle.penup()
    
    turtle.color("red")
    #Our turtle Color is the index of a color in Rainbow of a random number
    #that does not excede the length of rainbow.
    turtle.pendown()
    turtle.forward(num) #Draw the Number.
    turtle.goto(position[0],position[1])#goto Base of Column
    turtle.penup()
    

refreshGraph(numlist)
#Draw Graph initailly.


##Start of Bubble Sort


    
