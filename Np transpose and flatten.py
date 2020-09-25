# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import numpy
r,c = map(int,input().split())
arr = numpy.array([list(map(int,input().split())) for i in range(r)])
print(numpy.transpose(arr))
print(arr.flatten())
