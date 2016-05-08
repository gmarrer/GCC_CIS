#Gary Marrer
#This is my first python program with modules


#Each Python Function (module) must have () and end with colon :
def housekeeping():
    #identify global variables
    global firstNumber
    global secondNumber
    name = "student"
    firstNumber = 0
    secondNumber = 0
    average = 0
    
#must be defined before used 
def calculateAverage():
    #identify global variables
    global firstNumber
    global secondNumber
    global average
    
    #calculation logic
    average = (firstNumber + secondNumber) / 2
    
def mainLogic():
    #identify global variables
    global firstNumber
    global secondNumber
    global average

    #gather input
    firstNumber = input("Enter first number ")
    secondNumber = input("Enter second number ")
    calculateAverage()   #call calculate module 
    
def finishUp():
    #identify global variables
    global average

    #print the solution
    print "Average is ", average

# start of main program PROCESSING STARTS HERE

housekeeping()
mainLogic()
finishUp()

#eop
