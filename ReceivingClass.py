#Receiving class
"Receiving Class"
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
	
#end receiving class	If you'd have 