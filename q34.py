# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
import numpy
n = int(input())
a = []
b = []
for i in range(n):
    x = input().split()
    a.append(x) 
for i in range(n):
    y = input().split()
    b.append(y)
num_a = numpy.array(a,dtype=int)
num_b = numpy.array(b,dtype=int)
print(numpy.dot(num_a,num_b))
