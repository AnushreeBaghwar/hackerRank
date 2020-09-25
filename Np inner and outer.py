# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import numpy

a = input().split()
b = input().split()
num_a = numpy.array(a,dtype=int)
num_b = numpy.array(b,dtype=int)
print(numpy.inner(num_a,num_b))
print(numpy.outer(num_a,num_b))