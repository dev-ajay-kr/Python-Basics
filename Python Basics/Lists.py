list1 = ['Prince', 'Grace', 1999, 1998]
list2 = [1, 2, 3, 4, 5]
list3 = ["A1", "B2", "C3", "D4"]
# Accessing
print(list1[3])
print(list2[1:4])
# Updating
list1[2] = 2022
print("The new value of list[2] is", list1[2])
#################################################
# Deleting
del list1[0]
print("The list after deleting the index 0:")
print(list1)
################################
# ------------OPerators in Python List_----------------#
############################
print(len(['a', 'b', 'c']))
print([1, 2, 3] + [4, 5, 6])
print(['Hey!'] * 4)
print("3 in [1, 2, 3]   => to return boolean value\n and result id :-->", 3 in [1, 2, 3])
for x in [1, 2, 3]: print(x)

###########    Some more example for access

list1 = ['code', 'Code', 'CODE!']
print("list1 = ['code', 'Code', 'CODE!']")
print(list1[2])  # accessing in a directio
print(list1[-2])  # reversed
print(list1[1:])  # before or after :

##############################################
# ------------Methods
##############################################

list1 = ['Prince', 'Grace', "1990", "2000", "2022"]
# append
list1.append("1999")
print(list1)

# count
print(list1.count("2000"))

# extend
list2 = ['banana', 'apple', 'orange']
list1.extend(list2)
print(list1)

# index
print(list1.index("2000"))

# insert
list1.insert(1, "5000")
print(list1)

# pop
print(list1.pop())

# remove
list1.remove("2000")
print(list1)

# reverse
list1.reverse()
print(list1)

# sort
list1.sort()
print("sorting", list1)

# Function	              Description
# cmp(list1, list2)	Elements from both lists are compared.
# len(list)	This function returns the overall length of the list.
# max(list)	Returns the item from the list with the maximum value.
# min(list)	Returns the item from the list with the minimum value.
# list(seq)	A tuple is converted into a list.
# Python List Methods
# The following list methods are supported by Python:
#
# Methods	Description
# list.append(obj)	Append method Adds the object obj to the list
# list.count(obj)	Returns the number of times obj appears in the list.
# list.extend(seq)	The contents of seq are added to the list.
# list.index(obj)	The lowest index in the list at which obj occurs.
# list.insert(index, obj)	Inserts object obj at offset index into list
# list.pop(obj=list[-1])	Removes and returns the final object or obj from the list and returns it.
# list.remove(obj)	Removes the object obj from the list.
# list.reverse()	Objects in the list are reversed in place.
# list.sort([func])	Objects in the list are reversed in place.
#
#
# List comprehension is a simple and elegant way to make a new list out of an existing list in Python. An expression followed by a for statement enclosed in square brackets constitutes a list comprehension.
#
# Example:

sample = [2 ** i for i in range(5)]
print(sample)

sample = []
for i in range(5):
    sample.append(2 ** i)
print(sample)
# both will have sane output
