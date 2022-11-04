# these are anonymus function that can take any parameters
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


########

# Helps in code reusabilities
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

