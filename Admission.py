
#By Clyric Allen#
#This code is for determinig if someone is old enough to see a movie#

Age = int(input("How old are you?"))

if Age <= 4:
    print("Admission is free.")

elif Age > 4 and Age < 18:
        print("Admission is $20.00")

else :
            print ("Admission is $40.00.")
