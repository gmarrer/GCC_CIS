# #ArrayChoice.py
#Using an Array to make decisions
### testing GIT
#Use Parallel Arrays
myArrayKey = [1,2,3]
#                 0      1       2
myArrayValue = ["Dog", "Cat", "Fish"]
cnt = 0

while cnt <= 2:
    print ("Loop iteration - Subscript ", cnt)
    if (myArrayKey[cnt] == 2):
        print ("Found it: ", myArrayValue[cnt])
        break
    else :
        print ("Not Found")

    cnt = cnt + 1
