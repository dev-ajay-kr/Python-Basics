#By far best datatypes
#By following we can initialize set
x = {}
y = set({'Python', 'is', 'Fun'})
z = set(['India', 'Philippines'])
print(x,"\n", y, "\n", z)


#modification
y.add("aparamtly")
print(y)
y.update("I", "was", "Just", "kidding")
print(y)

#Deleting
###-- discard to remove element (if note present does nothing)
###-- remove (throw error if element is not present)
set1 = {'Prince', 'Adones', 'Jude', 'Paul', 'Ted', 'Glen', 'Jaymar'}

set1.discard('Adones')
print('using discard',set1) # discard an element

set1.remove('Ted')
print('using remove',set1) # remove an element

set1.discard('George')
print('discarding an element that is not present in set1',set1) # discard an element not present in set1

set1.remove('George') # remove an element not present in set1, you will get an error.

#######################################################
#####POP AND CLEAR ----------#
set1 = {'Prince', 'Adones', 'Jude', 'Paul', 'Ted', 'Glen', 'Jaymar'}

print(set1.pop())
# pop an random element

# clear set1
set1.clear()
print('After clearing:',set1)
# this will empty the set










############################################################################
############
# ###########Python Set Operations
# ########---------Python sets can be operated on using union, intersection, difference, and symmetric difference. These operations can be performed using either operators or methods.




##############---Union
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
# using the | operator
print(A | B)
# using the union function
print(A.union(B))


###############-------intersection
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
# using the & operator
print(A & B)
# using the intersection function
print(A.intersection(B))

#####-----Diffeence
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}

# using the - operator on A
print(A - B)

# using the - operator on B
print(B - A)

# using the difference function on A
print(A.difference(B))

# using the difference function on B
print(B.difference(A))


#######--------Symmetric Differemce ((Except the intersection))
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
# using the ^ operator on A
print (A ^ B)
# using the symmetric_difference function
print(A.symmetric_difference(B))

################ SOME MORE METHODS











# Methods	Description
# add()	Adds an element to the set
# clear()	Removes all elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raises a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Returns the union of sets in a new set
# update()	Updates the set with the union of itself and others