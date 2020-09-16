# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
result = []
for i in range(int(input())):
    operation =input().split()
    if operation[0] == 'append':
        d.append(operation[1])
    elif operation[0] == 'appendleft':
        d.appendleft(operation[1])
    elif operation[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print(" ".join(d))


