#It is something like lists only
# only thing is it is ordered and has unique identifier for each element
tuple1 = ("Prince", "Grace", 1999, 1998)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ('A1', 'B2', 'c3', 'D4')


#Accesing tuple
print (tuple1[3])
print (tuple2[1:4])

#Updation    :-------->  Updation isn't allowed once defined
#-----> however two can be merged
tuple3 = tuple1 + tuple2
print (tuple3)


tuple1 = ['Prince', 'Grace', 1999, 1998];
print (tuple1)
del (tuple1)
print ('The output below will prompt an error bwcause tuple is deleted')
#print (tuple1)


#indexing is similar
tuple1 = ('code', 'Code', 'CODE!')

# Offsets start at zero
print(tuple1[2])

# Negative: count from the right
print(tuple1[-2])

# Slicing fetches sections
print(tuple1[1:])

########## Function
tuple1 = ('Prince', 'Grace', 'Mario', 'Ludy', 'Mc  Quinn')
# cmp is not support in Python 3 but it is still workiin in Python 2
# len
print (len(tuple1))
# max
print (max(tuple1))
# min
print (min(tuple1))


list1 = ['Prince', 'Grace', 'Mario', 'Ludy', 'Mc  Quinn']
# tuple
print (tuple(list1))






