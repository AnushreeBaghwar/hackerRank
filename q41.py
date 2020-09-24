# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n = int(input())

for i in range(n):
    num = input()
    print(bool(re.match("^[+-]?[0-9]*\.[0-9]+$",num)))

