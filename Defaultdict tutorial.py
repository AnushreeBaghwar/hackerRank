# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
for i in range(1,n+1):
    d[input()].append(i)
for i in range(1,m+1):
    l = input()
    if(len(d[l]))>0:
        print(" ".join(str(i) for i in d[l]))
    else:
        print("-1")
