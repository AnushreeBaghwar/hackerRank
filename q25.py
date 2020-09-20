# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,n = input().split()

for i in range(1,int(n)+1):
    for k in combinations(sorted(s),i):
        print("".join(k))
