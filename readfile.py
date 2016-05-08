# reading a file

myFile = open("datafile.txt", "r")   #open file for read
cnt = 1
name  = 999
while name != "":
    name = myFile.read(19)
    street = myFile.read(20)
    city = myFile.read(20)
    state = myFile.read(2)
    x = myFile.read(1)

    print("Name   -->",name)
    print("street -->",street)
    print( "City   -->",city)
    print( "State  -->",state)
    cnt = cnt + 1
myFile.close()  #close file