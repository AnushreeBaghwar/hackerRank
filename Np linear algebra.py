# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
import numpy

numpy.set_printoptions(legacy='1.13')
n = int(input())
a = []
for i in range(n):
    x = input().split()
    a.append(x)
num = numpy.array(a,dtype=float)
print(numpy.linalg.det(num))

