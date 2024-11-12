#Task #1
#Write a program to take a user age and let him know if he can go the club.  21
print("According to the age constraints we can tell if you are eligible to enter into the CLUB")
age= int(input("Enter your age to know the Eligibility : "))

if age <21:
    print("Oops sorry, You can come again after" ,21-age,"Years")
else:
    print("You are welcome to the CLUB... :-)")