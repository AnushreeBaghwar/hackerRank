# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
import numpy

def arrays(arr):
    output = numpy.array(arr[::-1],dtype=float)
    return output
arr = input().strip().split(' ')
result = arrays(arr)
print(result)