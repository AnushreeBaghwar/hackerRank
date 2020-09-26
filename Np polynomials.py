# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
import numpy
p = numpy.array(list(map(float,input().split())))
x = float(input())
print(numpy.polyval(p,x))


