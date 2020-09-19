
# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
li = list(map(int,input().split()))
n = int(input())
money = 0
for i in range(n):
    shoe_size = Counter(li)
    size,cost = map(int,input().split())
    if size in shoe_size:
        li.remove(size)
        money+=int(cost)
print(money)

