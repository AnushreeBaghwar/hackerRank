# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,k = input().split()
output = list(combinations_with_replacement(sorted(s),int(k)))
result = sorted(output)
for i in result:
    print("".join(i))