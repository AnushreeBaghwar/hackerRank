# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
for i in range(num):
    try:
        a,b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
