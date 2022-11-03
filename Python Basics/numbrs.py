n_pieces = int(input("How many pieces of the pumpkin pie can I offer you?"))
##############
num1 = 1234
num2 = 12.34
print(type(num1))
print(type(num2))
# Number Data Types in Python
# There are three number data types in Python:
# Integer
# Float
# Complex

var1 = 751
var2 = -8712
print (var1)
print ("The var1 data type is {}".format(type(var1)))
print (var2)
print ("The var2 data type is {}".format(type(var2)))
#
# Python offers integer data types for various number systems, such as binary, octal, and hexadecimal.
# We can represent binary numbers in Python by prefixing the number with 0b, as in 0b1110, hexadecimal numbers by prefixing the number with 0x, as in 0x1117, and octal numbers by prefixing the number with 0o, as in 0o1117.
var1 = 1117
var2 = 0x1117
var3 = 0o1117
var4 = 0b1110

print("Data Type of 1117 is {}".format(type(var1)))
print("Data Type of 0x1117 is {}".format(type(var2)))
print("Data Type of 0o1117 is {}".format(type(var3)))
print("Data Type of 0b1110 is {}".format(type(var4)))


###-----float
var1 = 123.14
print (var1)
print ("The var1 data type is {}".format(type(var1)))


#####-------- COmplex number----
#------- of form a+ib



var1 = 6+5j
var2 = 9j
var3 = -7j

print(type(var1))
print(type(var2))
print(type(var3))

var1= complex(3,2)  ## it'll convert to cmplex number\

print(var1,type(var1))

var1= complex(3,2)
realnum = var1.real
imagnum = var1.imag
print(var1)
print("Real number is ", realnum)
print("Imaginary number is ", imagnum)



#------------------
var1= complex(3,2)
conjugateNum= var1.conjugate()
print(var1)
print("Conjugate is", conjugateNum)

#########
#-Fractions
############

import fractions

var1 = fractions.Fraction(1,2)
print("var1 answer is",var1)
print(type(var1))

