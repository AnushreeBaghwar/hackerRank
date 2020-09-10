# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_eng = int(input())
roll_eng = set(map(int,input().split()))
num_french = int(input())
roll_french = set(map(int,input().split()))
result = roll_eng.difference(roll_french)
print(len(result))