# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__=='__main__':
    S = input()
print(any(i.isalnum() for i in S))
print(any(i.isalpha() for i in S))
print(any(i.isnumeric() for i in S))
print(any(i.islower() for i in S))
print(any(i.isupper() for i in S))
