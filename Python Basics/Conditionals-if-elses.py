###bool values


a = 100
if a:
   print ("1 - Got a true expression value")
   print (a)

b = 0
if b:
   print ("2 - Got a true expression value")
   print (b)
print ("Done!")
############################################################
a = 15
b = 20

if a > b:
    #False block
    print("a is greater")
else:
    #True block
    print("b is greater")

############  if-elif-else

a=15
b=15
if a>b:
    print("a is greater")
elif a==b:
    print("both are equal")
else:
    print("b is greater")

###########-Nested-if

num=5
if num>=0:
    if num==0:
        print(" its zero bro")
    else:
        print(" It should be positive ")
else:
    print("negative number")


########-single line if condition

a = 20

if (a == 20): print("The value of a is 20")