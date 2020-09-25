# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
import numpy
n,m = map(int,input().split())
arr = []
for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
num = numpy.array(arr)
num_sum = numpy.sum(num,axis=0)
print(numpy.prod(num_sum))


