# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_eng_sub = int(input())
roll_eng_sub = set(map(int,input().split()))
num_fren_sub = int(input())
roll_fren_sub =set(map(int,input().split()))
result = roll_eng_sub.symmetric_difference(roll_fren_sub)
print(len(result))