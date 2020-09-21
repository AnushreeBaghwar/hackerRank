# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
import numpy
n,m = map(int,input().split())
arr=[]
for i in range(n):
    x = input().split()
    arr.append(x)
res = numpy.array(arr,dtype=int)
mini = numpy.min(res,axis=1)
print(numpy.max(mini))

