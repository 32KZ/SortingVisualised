##Original Code By Victoria Miller aka Juuls
##Edits Made By 32KZ

##Imports
import turtle
import random
import time

##Classes

class MyTurtle:
    def __init__(self, color="black"):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.speed(0)
        

    def forward(self, distance):
        self.turtle.forward(distance)

    def backward(self, distance):
        self.turtle.backward(distance)

    def left(self, angle):
        self.turtle.left(angle)

    def right(self, angle):
        self.turtle.right(angle)

    def set_color(self, color):
        self.turtle.color(color)

    def penup(self):
        self.turtle.penup()

    def pendown(self):
        self.turtle.pendown()

    def done(self):
        turtle.done()

##Functions
        
def refreshGraph(numlist, ourTurtle):
  ourTurtle.turtle.goto(-250,0)
  for num in numlist:
    #realign the turtle 10PX to the right.
    myxpos = ourTurtle.turtle.xcor()
    ourTurtle.turtle.setx(myxpos + 10)
    position = ourTurtle.turtle.pos() #Save Position of turtle in X and Y as [0],[1]
    
    ourTurtle.turtle.pd()
    ourTurtle.turtle.color("white") #Clear the collumn
    ourTurtle.turtle.forward(151)
    ourTurtle.turtle.goto(position[0],position[1]) #Go to base of Column
    ourTurtle.turtle.penup()
    
    ourTurtle.turtle.color("red")
    #Our turtle Color is the index of a color in Rainbow of a random number
    #that does not excede the length of rainbow.
    ourTurtle.turtle.pendown()
    ourTurtle.turtle.forward(num) #Draw the Number.
    ourTurtle.turtle.goto(position[0],position[1])#goto Base of Column
    ourTurtle.turtle.penup()
    
        
##Variables
mainTurtle = MyTurtle("red")
numlist = []

##Main

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



refreshGraph(numlist, mainTurtle)
#Draw Graph initailly.


##Start of quicksort

def quicksort(numlist):
    if len(numlist) <= 1:
        return numlist  # Base case: if the array has 0 or 1 element, it is already sorted

    pivot = numlist[len(numlist) // 2]  # Choose the pivot element (here, we select the middle element)

    # Divide the array into two sub-arrays, based on the pivot element

    smaller = [x for x in numlist if x < pivot]  # Elements smaller than the pivot
    equal = [x for x in numlist if x == pivot]   # Elements equal to the pivot
    greater = [x for x in numlist if x > pivot]  # Elements greater than the pivot

    currentList = smaller + equal + greater

    our_turtle = MyTurtle("red")
    refreshGraph(currentList, our_turtle)
    # Recursively sort the sub-arrays
    return quicksort(smaller) + equal + quicksort(greater)
    # Combine the sorted smaller, equal, and greater arrays

sorted_array = quicksort(numlist)
print(sorted_array)


##TO DO
## make it able to run different turtles at the same time
## create turtles through classes
## make more efficient
## add more sorts
## add gui
## 
    
