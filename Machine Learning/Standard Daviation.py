#the range to show how spread are other values to the mean values
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)
y = numpy.std(speed)

print(x)
print(y)