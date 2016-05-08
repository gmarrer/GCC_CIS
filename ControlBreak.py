# Gary Marrer
# ControlBreak.py
# Program takes to inputs for control break processing example
# GCC


# module definition section
# modules are not executed until called
# but have to be defined before they are used
def houseKeeping():  # houseKeeping module/function
	print "housekeeping called"
	global partNum
	global partAmt
	global oldPartNum
	global partGrandTot
	global partAmtTot
	global cnt
	global output
	
	partAmtTot = 0   #running total for each part number
	partGrandTot = 0  #grand total of all parts
	cnt= 1 # cnt is used for screen output
	
	print "Parts Report - Control Break"    #report title

	#output variable set to allow print to text file
	output = open("output.txt","w")   # varible to write to a text file
	print >> output, "Parts Report - Control Break"  #>> means print to file
	print >> output, "Part#    Amount "
	
	partNum = input("Part Number (-1 to Quit) ")  #get part number from keyboard
	partAmt = input("Enter Part Amount ") # get part amoutn from keybaord
	oldPartNum = partNum   # setup for control break processing
	
	
def contBrk():  #control break module/function
	global partNum
	global partAmtTot
	global partGrandTot
	global partAmt
	global oldPartNum
	global output
	
	# PRint to Screen
	print "Control Break"
	print "Part#    Amount "
	print oldPartNum, "       ", partAmtTot
	
	# Print to File
	print >> output, "Sub Total >>> ", oldPartNum, "       ", partAmtTot

	# accumlate for grand total 	
	partGrandTot = partGrandTot + partAmtTot

	#reset control break variable to new part number
	oldPartNum = partNum
	
def mainLoop():  # mainloop module
	print "main Loop called"

	#set up variables
	global partNum
	global partAmt
	global oldPartNum
	global partAmtTot 
	global partGrandTot
	global cnt
	global output

	#test for control break
	if partNum != oldPartNum:
		contBrk()
		partAmtTot = 0

	# Print to screen
	print "--------------------------"
	print "Part#    Amount  Count"
	print partNum, "       ", partAmt, "    ", cnt
	#Print to File
	print >> output, partNum, "       ", partAmt
	
	partAmtTot = partAmtTot + partAmt  # accumulate running total for part
	
	#read next Record
	partNum = input("Part Number (-1 to Quit) ")
	if partNum != -1:        #if -1 for partNum then ignore this prompt
		partAmt = input("Enter Part Amount ")
		cnt = cnt + 1 

def finishUp():  # finishup module
	global partGrandTotal
	global output
	# call for one more control break for display and correct grand total
	contBrk()
	# Print to Screen
	print "Grand Total ", partGrandTot, "  Part Count= " , cnt

	# Print to File
	print >> output, "Grand Total >>> ", partGrandTot,  " Part Count= " , cnt

	#close file
	output.close()

	print "E O P"

#main program logic  --- start of programming logic

#  PROGRAM STARTS EXECUTION HERE!
houseKeeping()  #call houseKeeping()

# Test to continue loop or process finish up
while partNum != -1:
	#call mainLoop
	mainLoop()
	
#call finish up
finishUp()

#eop


