#Chapter 3 Rev Question 15

day = ""
time = ""
print "Enter times and days to test logic"
day = raw_input("Enter day (Monday - Sunday)")
time = input("Enter time ")

if (time == 8) and (day == "Monday") or (day == "Friday"):
    print "true"
else:
    print "false"
            