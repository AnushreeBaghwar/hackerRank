# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_sub = int(input())
roll_eng = set(map(int,input().split()))
fren_sub = int(input())
roll_fren = set(map(int,input().split()))
result = roll_eng.intersection(roll_fren)
print(len(result))