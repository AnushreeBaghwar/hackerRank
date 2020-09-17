# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
a = set(map(int,input().split()))
for i in range(int(input())):
    b,c = input().split()
    cmd = set(map(int,input().split()))
    if b=="intersection_update":
        a.intersection_update(cmd)
    elif b=="update":
        a.update(cmd)
    elif b=="symmetric_difference_update":
        a.symmetric_difference_update(cmd)
    else:
        a.difference_update(cmd)
print(sum(a))