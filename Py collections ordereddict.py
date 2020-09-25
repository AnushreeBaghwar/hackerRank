# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
my_items = OrderedDict()

for i in range(int(input())):
    item = input().split()
    cost = int(item[-1])
    name = " ".join(item[:-1])

    if name not in my_items:
        my_items[name]=cost
    else:
        my_items[name]+=cost
for i,j in my_items.items():
    print(i,j)