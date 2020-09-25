# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    N = input().split()
    if N[0]=="pop":
        s.pop()
    elif N[0]=="remove":
        s.remove(int(N[1]))
    else:
        s.discard(int(N[1]))
print(sum(s))