# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s = input().split()
output = list(permutations(s[0],int(s[1])))
x=  sorted(output)

for i in x:
    print("".join(i))

