import datetime

x = datetime.datetime.now()
print(x)    #3 PRINTSCOMPLETE DATES

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))  ##---Day
#     The datetime object has a method for formatting date objects into readable strings.
print(x.strftime("%B"))  ##---Day
print(x.month)
print(x.day)
print(x.fold)

# a date object
y = datetime.datetime(2020, 5, 17)

print(y)
###############
#----------Directives
##############

print(x.strftime("%a"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%y"))
print(x.strftime("%p"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%V"))


