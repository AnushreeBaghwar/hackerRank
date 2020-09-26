# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
import numpy
numpy.set_printoptions(legacy='1.13')
a = input().split()
num_a = numpy.array(a,dtype=float)
print(numpy.floor(num_a))
print(numpy.ceil(num_a))
print(numpy.rint(num_a))

