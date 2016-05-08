class BikeClass: 
	# instance variables   -------------------------------------------- #
	name = ""
	model = ""
	ticketNumber = 0 
	cost = 0 
	
	# method  -------------------------------------------------------- #
	def getName():
		return name
	def setName(self, inName):
		if inName != "":
			name = inName
		else:
			print "Invalid - Name Required"
	def getModel():
			return model
	def setModel(self, inModel):
		if (inModel != "") :
			model = inModel
		else:
			print "Invalid - Model Required"
	def getTicketNumber():
		return ticketNumber
	def setTicketNumber(self, inTiecketNumber):
		if (inTicketNumber != ""):
			ticketNumber = inTicketNumber
		else:
			print "Invalid - Ticket Number Required"
	def getCost():
		return cost
	def setCost(self, inCost):
		if inCost <= 0 :
			cost = inCost
		else:
			print "Invalid - Cost must be greater than zero"
			
#end of class