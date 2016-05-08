#FileMerge.py

def readFruit1():
	 global name1
	 global calories1
	 global fruit1
	 name1 = fruits1.read(8)
	 calories1 = fruits1.read(3)
	 if name1 == "":
	     name1 = "ZZZZ"
	 print ("record 1 >> " , name1, "  ", calories1)


def readFruit2():
	  global name2
	  global calories2
	  global fruit2
	  name2 = fruits2.read(8)
	  calories2 = fruits2.read(3)
	  if name2 == "":
	     name2 = "ZZZZ"
	  print ("record 2 >> " , name2, "  ", calories2)


#start of program

name1 = ""
name2 = ""
calories1 = ""
calories2 = ""
outVar =""

fruits1 = open("fruit1.txt", "r")
fruits2 = open("fruit2.txt", "r")
outFile =open("fruits.txt","a")
bothAtEOF = "N"
readFruit1()
readFruit2()

while bothAtEOF != "Y":
	if (name1 < name2):
		outVar = name1 + calories1
		outFile.write(outVar)
		print ("Fruit1 ", name1, "  ", calories1)
		readFruit1()
	else:
		outVar = name2 + calories2
		outFile.write(outVar)
		print ("Fruit2 ", name2, "  ", calories2)
		readFruit2()

	if name1 == "ZZZZ":
		if name2 == "ZZZZ":
			print ("hit")
			bothAtEOF = "Y"

fruits1.close()
fruits2.close()
outFile.close()
print ("EOP")
