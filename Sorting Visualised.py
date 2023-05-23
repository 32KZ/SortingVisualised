##Imports
import turtle
import random
import time

##Main

##Variables
turtle.speed(10000)
numlist = []

##


# until our list is length 50,
# add a random number from 0-150 thats not already in list.

while len(numlist) != 50:
  num = random.randint(0,150)
  if num not in numlist:    
    numlist.append(num)


    
rainbow =["violet","pink","indigo"]

turtle.left(90)
turtle.penup()
turtle.goto(-200,0)
turtle.width(10)
turtle.pendown()


def drawgraph(rainbow,numlist):
  for num in numlist:
    position = turtle.pos()

    turtle.color("white")
    turtle.forward(200)
    turtle.goto(position[0],position[1])

    turtle.color(rainbow[random.randint(0,(len(rainbow))-1)])
    turtle.forward(num)
    turtle.goto(position[0],position[1])
   
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

drawgraph(rainbow,numlist)

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
    if passes % 200 == 0:
      drawgraph(rainbow,numlist)
     
print(numlist)
print(passes)
drawgraph(rainbow,numlist)
