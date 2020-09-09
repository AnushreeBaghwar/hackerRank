# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        cmd = input().split()
        inp = cmd[0]
        if inp=="insert":
            arr.insert(int(cmd[1]),int(cmd[2]))
        elif inp=="remove":
                arr.remove(int(cmd[1]))
        elif inp=="append":
            arr.append(int(cmd[1]))
        elif inp=="sort":
            arr.sort()
        elif inp=="pop":
            arr.pop()
        elif inp=="reverse":
            arr.reverse()
        elif inp=="print":
            print(arr)