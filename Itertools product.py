# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c=a,b
data = product(*c)
print(*data)

