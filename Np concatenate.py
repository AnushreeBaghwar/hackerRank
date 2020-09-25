# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
import numpy
n,m,p = map(int,input().split())
np = numpy.array([list(map(int,input().split())) for i in range(n)])
mp = numpy.array([list(map(int,input().split())) for i in range(m)])
print(numpy.concatenate((np,mp),axis=0))    


