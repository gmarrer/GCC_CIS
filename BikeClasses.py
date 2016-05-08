#Bike Classes Module
class BikeClass: 
	# instance variables   -------------------------------------------- #
	def __init__(self ):
		self.name = ""
		self.model = ""
		self.ticketNumber = 0 
		self.cost = 0 
	
	# method  -------------------------------------------------------- #
	def getName(self):
	    return self.name
	def setName(self, inName):
	    if inName != "":
		self.name = inName
	    else:
		print "Invalid - Name Required"
	def getModel(self):
		return self.model
	def setModel(self, inModel):
	    if (inModel != "") :
		self.model = inModel
	    else:
		print "Invalid - Model Required"
	def getTicketNumber(self):
	    return self.ticketNumber
	def setTicketNumber(self, inTicketNumber):
	    if (inTicketNumber != ""):
		self.ticketNumber = inTicketNumber
	    else:
		print "Invalid - Ticket Number Required"
	def getCost(self):
	    return self.cost
	def setCost(self, inCost):
	    if inCost > 0 :
		self.cost = inCost
	    else:
		print "Invalid - Cost must be greater than zero"
			
#end of class
