# reading a file with global local

myFile = open("datafile.txt", "r")   #open file for read
name = 0

def main() :
    cnt = 1
    while name != "":
        #global var
        global name

        #print ("Name " ,name)
        name = myFile.read(19)
        street = myFile.read(20)
        city = myFile.read(20)
        state = myFile.read(2)

        print ("Name   -->",name)
        print ("street -->",street)
        print ("City   -->",city)
        print ("State  -->",state)
        cnt = cnt + 1

main()
myFile.close()  #close file