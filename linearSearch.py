#LinearSearch.py
#Gary Marrer
#demonstration of bubble sort routine

#declare and intialize array of state codes
myArray = [12,22,23,99,1004]

# start of program

subscript = 0 #first element on an array
searchValue = 99

for subscript in myArray:
	if (subscript  == searchValue):
		print ("Found value", subscript)
		print ("at element", (myArray.index(99) + 1))
    #else :
        #print ("Not Found ", subscript)

