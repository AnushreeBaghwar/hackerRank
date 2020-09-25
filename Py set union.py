# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_sub = int(input())
roll_eng = set(map(int,input().split()))
fren_sub = int(input())
roll_fren = set(map(int,input().split()))
result = roll_eng.union(roll_fren)
print(len(result))