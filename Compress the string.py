# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for i,j in groupby(map(int,list(input()))):
    print(tuple([len(list(j)),i]),end=" ")