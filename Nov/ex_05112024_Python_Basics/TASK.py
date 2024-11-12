print("Hello world..!")
print(100*'-')
# print(self, *args, sep=' ', end='\n', file=None):
# *args:- Unlimited number of comma seperated arguments
# sep:- string inserted between values, default a space.
# end:- string appended after the last value, default a newline.
# file:- a file-like object (stream); defaults to the current sys.stdout.

print("Testing Academy", 9988776655, {"Course": "Python-SDET"},
      ["Python","Selenium","API"], ("NOTES","TASK"))
print(100*'-')
print("Testing Academy", 9988776655, {"Course": "Python-SDET"},
      ["Python","Selenium","API"], ("NOTES","TASK"), sep="--",end="\n")
print(100*'-')
print("Testing Academy", 9988776655, {"Course": "Python-SDET"},
      ["Python","Selenium","API"], ("NOTES","TASK"), sep="<>")