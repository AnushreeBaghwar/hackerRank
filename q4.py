# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)