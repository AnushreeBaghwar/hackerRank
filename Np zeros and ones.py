# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy
ls = list(map(int,input().split()))
print(numpy.array(numpy.zeros(ls,dtype=numpy.int)))
print(numpy.array(numpy.ones(ls,dtype=numpy.int)))    

