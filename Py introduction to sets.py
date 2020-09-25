# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
def average(array):
    set_arr = set(array)
    set_sum = sum(set_arr)
    length = len(set_arr)
    x = set_sum/length
    return x
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)