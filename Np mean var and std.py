# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
import numpy
numpy.set_printoptions(legacy='1.13')
n,m = input().split()
arr = []
for i in range(int(n)):
    x = list(map(int,input().split()))
    arr.append(x)
num = numpy.array(arr,dtype=int)
print(numpy.mean(num,axis=1))
print(numpy.var(num,axis=0))
print(numpy.std(num))

