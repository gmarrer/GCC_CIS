#ReceivingMain.py
#tkinter module implments TCL toolkit for GUI programming in PYTHON

#import Tkinter module to work with Tk GUI toolkit
from Tkinter import *
import tkMessageBox

#GUI Screen class
#class used to make this gui reusable
class MainScreen:
   
    #constructor receives root window
    def __init__(self, master):
        #instantiate frame with root window as the inherited parent
        frame = Frame(master)
        #set the text in the titlebar
        frame.master.title("Receiving Main")
        #display root window
        frame.pack()
        
        #instantiate ReceiveingLogic object 
	self.recvLogic = ReceivingLogic()
	
	 #stringVar is a control variable used to change text at run time    
	self.returnedOrder = StringVar()
        self.returnedOrder.set("Order Not Found!")

	 #create a label to display the calculation answer        
	self.orderNumLabel = Label(frame, width=15, fg="black",  text="Enter Order #" )
	 #grid method to set control visible, left justify
	self.orderNumLabel.grid(row=0, column=0, sticky=W)

        #create a entry control with width of 5 inside the frame object
        #the entry control creates a single line textbox for the order number
        self.orderNumber = Entry(frame, width=15)
        #grid method to set control visible, left justify
        self.orderNumber.grid(row=0, column=1, sticky=W)
        #set focus on the first textbox
        self.orderNumber.focus_set()
        
        #create a calc button control, label with calculate
	#set foreground color property to blue inside the frame object
	self.calc = Button(frame, text="Look Up ", fg="blue")
	 #grid method to set control visible, left justify
	self.calc.grid(row=0, column=2, sticky=W)
	#create button event
	#a left mouse click will look for the lookUpOrder function
	self.calc.bind("<Button-1>", self.lookUpOrder)
        
        #label box  
	self.errorMessageLabel = Label(frame, width=15, fg="red", relief = "ridge" )
	self.errorMessageLabel.grid(row=0, column=3, sticky=W)
	
	 #label box      
	self.vendorScrLabel = Label(frame, width=15, fg="black", text="Vendor" )
	self.vendorScrLabel.grid(row=1, column=0, sticky=W)

	 #label box         
	self.vendorLabel = Label(frame, width=15, fg="black"  )
	self.vendorLabel.grid(row=1, column=1, sticky=W)
	
	 #label box        
	self.vendorIDScrLabel = Label(frame, width=15, fg="black",  text="Vendor ID")
	self.vendorIDScrLabel.grid(row=2, column=0, sticky=W)

        # #label box          
       	self.vendorIDLabel = Label(frame, width=15, fg="black" )
	self.vendorIDLabel.grid(row=2, column=1, sticky=W)
       
        #label box        
       	self.locationScrLabel = Label(frame, width=15, fg="black", text="Location")
       	self.locationScrLabel.grid(row=3, column=0, sticky=W)
       
         #label box          
        self.locationLabel = Label(frame, width=15, fg="black"  )
	self.locationLabel.grid(row=3, column=1, sticky=W)
       
         #label box        
        self.openOrdersLabel = Label(frame, width=15, fg="black"  , text="Open Orders ")
	self.openOrdersLabel.grid(row=4, column=0, sticky=W)
        
	 #label box        
	self.openOrdersDataLabel = Label(frame, width=60, fg="black", textvariable=self.returnedOrder)
	self.openOrdersDataLabel.grid(row=4, column=1, sticky=W)
	 
	#set foreground color property to blue inside the frame object
	self.Process = Button(frame, text="Process Order", fg="blue")
	#grid method to set control visible, left justify
	self.Process.grid(row=5, column=0, sticky=W)
	#create button event
	#a left mouse click will look for the lookUpOrder function
        self.Process.bind("<Button-1>", self.callProcessOrder)
        
        #set foreground color property to blue inside the frame object
	self.Except = Button(frame, text="Process Exception", fg="blue")
	#grid method to set control visible, left justify
	self.Except.grid(row=5, column=1, sticky=W)
	#create button event
	#a left mouse click will look for the lookUpOrder function
	self.Except.bind("<Button-1>", self.callExcept)
	
	#set foreground color property to blue inside the frame object
	self.PrintOrder = Button(frame, text="Print Order", fg="blue")
	#grid method to set control visible, left justify
	self.PrintOrder.grid(row=5, column=2, sticky=W)
	#create button event
	#a left mouse click will look for the lookUpOrder function
	self.PrintOrder.bind("<Button-1>", self.callPrintOrder)
	
	#set foreground color property to blue inside the frame object
	self.Exit = Button(frame, text="End Program", fg="blue", command = root.quit)
	#grid method to set control visible, left justify
	self.Exit.grid(row=5, column=3, sticky=W)
      
    #event handlers for button clicks
    def lookUpOrder(self, event):
        #get a value from both entry contols and store in value1 and value2
	self.orderNum = str(self.orderNumber.get())
	self.recvLogic.setOrderNumber(self.orderNum)
	self.returnedOrder.set(self.recvLogic.lookUpOrder()  )
    
    def callProcessOrder(self, event):
        tkMessageBox.showinfo("Window Message", "Order Processed!") 
        self.returnedOrder.set(""  )
        self.orderNumber.focus_set()
        self.orderNumber.delete(0,99)
     	
    def callExcept(self, event):
    	tkMessageBox.showinfo("Window Message", "Display Exception Screen") 
     	
    def callPrintOrder(self, event):
     	tkMessageBox.showinfo("Window Message", self.recvLogic.lookUpOrder()) 
     	
    def callExit(self, event):
    	tkMessageBox.showinfo("Window Message", "Exit Program") 
 # end screen class    
      
#Receiving class
#class used to make this gui reusable
class ReceivingLogic:
    
	#instance variables
	def __init__(self ):
		self.qty = 0
		self.cost = 0
		self.orderNumber = "" 
		self.Vendor = ""
		self.VendorID = ""
		self.orderNumber =  0
		
		#---------------------------------------------------------------------------------------------------------------------------------------------#	
		# NOTE! BUILD AND INSTANITATE TEST DATA STORED IN AN TWO DIMENSIONAL STRING ARRAY 
			# ORDER NUMBER, DESC, VENDOR, VENDOR ID, QTY, LOCATION
		#---------------------------------------------------------------------------------------------------------------------------------------------# 

		self.ordersArray = [["A1", "Java Programming", "BOB BOOKS", "BB1", 12, 20],
			["A11", "Java Programming", "JAVA BOOKS", "BB1", 28, 25],
			["B1E11", "Visionary VB", "WORLD PUBLISHING","RDB1", 5, 12],
			["C32", "Cool COBOL", "COBOL CORP","CC41", 12, 35],
			["C56711", "Pasionate about PASCAL", "PETES PASCAL BOOKS", "G561", 12, 50],
			["GDM1", "Fundamentals of Programming", "GARY BOOKS","GDM", 12, 56],
			["GH90", "Perfect PYTHON", "BOB BOOKS","PY101", 12, 24],
			["BD4", "REXX Programming", "REXX PUBS","MBI3", 32, 6],
			["F433", "JavaScript Programming","JAVA GREATS", "JS45", 12, 5],
			["NM6", "Assembly Programming in 4 Seconds", "BETTER BOOKS","A2S", 2, 200]]
		#---------------------------------------------------------------------------------------------------------------------------------------------# 
			
	# Accessor and mutator methods

	def setQty(self, inVar):
		if (inVar <0 ):
			self.qty = inVar
		else:
			print "Invalid Quantity"

	def getQty(self):
		return self.qty
	#	

	def setCost(self, inVar):
		if (inVar <0 ):
			self.cost = inVar
		else:
			print "Invalid Cost"

	def getCost(self):
		return self.cost
	#	 

	def setOrderNumber(self, inVar):
		if (inVar != "" ):
			self.orderNumber = inVar
		else:
			print "Invalid Order Number"

	def getOrderNumber(self):
		return self.orderNumber
		
	#	 

	def setVendor(self, inVar):
		if (inVar !="" ):
			self.vendor = inVar
		else:
			print "Invalid Vendor Name"
	#
	
	def getVendor(self):
		return self.vendor
	#	
		
	def setVendorID(self, inVar):
		if (inVar !="" ):
			self.vendorID = inVar
		else:
			print "Invalid VendorID"
	
	def getVendorID(self):
		return self.vendorID
	#	

	def lookUpOrder(self):
		searchVar = 0 
		cnt = 0
		foundValue = "Order Number not Found"
		
		for searchVar in self.ordersArray:
			if  searchVar[0].upper() == self.orderNumber.upper() :
				foundValue = str(searchVar[0] ) + "  |   " + str(searchVar[1]) + "  |   " + str(searchVar[2] )+ "  |   " + str(searchVar[3] )+"  |   " + str(searchVar[4] )
			cnt = cnt + 1
	
		return foundValue
	
#end receiving class	
	
#start of program

#root represents the base GUI window
root = Tk()

#create a instance of calculateProgram and pass it the root window
app = MainScreen(root)

#event loop
#program is now waiting for input/events from root window
root.mainloop()
