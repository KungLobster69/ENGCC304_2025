#START
    #PRINT "ENTER YOUR AGE"
    #READ AGE
#IF AGE >= 18 THEN
    #PRINT "YOU ARE ELIGIBLE TO VOTE"
#ELSE
    #PRINT "YOU ARE NON-ELIGIBLE TO VOTE"
#ENFIF
#END

age_str = input("Please enter your age: ")
age = int (age_str)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

years_left = 18 - age
print ("You will be eligible in", years_left, "years.")