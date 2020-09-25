# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
import numpy

n,m = input().split()
a = []
b = []
for i in range(int(n)):
    x = input().split()
    a.append(x)
for i in range(int(n)):
    y = input().split()
    b.append(y)
num_a = numpy.array(a,dtype=int)
num_b = numpy.array(b,dtype=int)
print(numpy.add(num_a,num_b))
print(numpy.subtract(num_a,num_b))
print(numpy.multiply(num_a,num_b))
print(num_a//num_b)
print(numpy.mod(num_a,num_b))
print(numpy.power(num_a,num_b))

