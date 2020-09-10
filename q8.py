# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = divmod(a,b)
for i in c:
    print(i)
print(c)