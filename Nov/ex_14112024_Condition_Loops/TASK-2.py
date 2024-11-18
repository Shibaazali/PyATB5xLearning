'''Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine
if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene
(no sides are equal). Use an if-else statement to classify the triangle.'''

s1= int(input("Enter the side 1: "))
s2= int(input("Enter the side 2: "))
s3= int(input("Enter the side 3: "))

if (s1==s2 and s2==s3 and s3==s1):
    print("Equilateral triangle")
elif (s1==s2 or s2==s3 or s3==s1):
    print("Isoceles triangle")
elif (s1!=s2 and s2!=s3 and s3!=s1):
    print("Scalene triangle")
else:
    print("Invalid input provided")