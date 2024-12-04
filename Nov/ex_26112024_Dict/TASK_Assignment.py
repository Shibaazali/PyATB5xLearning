# Sort a dictionary by its values in descending order
from audioop import reverse

my_dict = {"a": 3, "b": 1, "c": 2}

output = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# printing output
print(output)

'''***************************************************'''

'''Question 2 : 
my_list = [1, 2, 2, 3, 4, 4, 5]
Remove duplicates from a list using a set.
Output: [1, 2, 3, 4, 5]'''

my_list = [1, 2, 2, 3, 4, 4, 5]
Dup = set(my_list)
print(Dup)

