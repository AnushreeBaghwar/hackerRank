# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
import re 
n = int(input())

for i in range(n):
    num = input()
    if num.isnumeric() and len(num)==10 and re.findall("\A[7-9]",num):
        print("YES")
    else:
        print("NO")