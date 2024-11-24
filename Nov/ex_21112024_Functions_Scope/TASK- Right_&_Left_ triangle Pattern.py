''' Program to print the right triangle pattern '''
rows = int(input("Enter the number of rows : "))

for row in range(0,rows):
    #display *
    for star in range(0,row+1):
        print("*", end="")
    print()
#################################################################
''' Program to print the left triangle program '''
l_rows = int(input("Enter the number of rows : "))
for l_row in range(1,l_rows+1):

    # To display the spaces:
    for space in range(1,(l_rows-l_row)+1):
        print(" ", end="")

    #To display the stars:
    for star in range(1,l_row+1):
        print("*", end="")
    print()