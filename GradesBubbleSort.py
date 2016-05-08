#GradesBubbleSort.py
#Gary Marrer
#demonstration of bubble sort routine

#declare and intialize array of grades
arrayOfGrades = [76, 86, 91, 67, 96]

#declare and initialize variables
arrayElements = len(arrayOfGrades)  -1     #element pairs
tempSwapVar = ""
moreFlag = 1

#counters for loop processing
outerCnt = 0
innerCnt = 0
 
#sort in Assending Order
while outerCnt < arrayElements and moreFlag == 1:  #count one less then numbe of elements
    moreFlag = 0
    while (innerCnt < arrayElements ):
        if (arrayOfGrades[innerCnt ] > arrayOfGrades[innerCnt + 1]):
            print "swap... ", arrayOfGrades[innerCnt ], "  " , arrayOfGrades[innerCnt + 1]
            #if next element is less then current then swap order in array
            tempSwapVar = arrayOfGrades[innerCnt]
            arrayOfGrades[innerCnt] = arrayOfGrades[innerCnt + 1]
            arrayOfGrades[innerCnt + 1] = tempSwapVar
            moreFlag = 1
        innerCnt = innerCnt + 1
        print arrayOfGrades[0], "  ",  arrayOfGrades[1], "  ", arrayOfGrades[2], "  ", arrayOfGrades[3], "  ", arrayOfGrades[ 4] 
    outerCnt = outerCnt + 1
    print "outer loop ", outerCnt
    innerCnt = 0
    
print "Print Array in Ascending Order"
for grades in arrayOfGrades:
    print grades
   



