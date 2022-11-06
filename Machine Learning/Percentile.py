# (i.e. 70th percentile refers to your child being heavier than 70% of all other children at his height).import numpy
# percentile is actually ranking and percentage is marking :)L̥L̥
# What is the age that 90% of the people are younger than?
import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = numpy.percentile(ages, 90)  
print(x)
