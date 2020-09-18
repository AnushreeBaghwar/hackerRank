# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def print_formatted(number):
    # your code goes here
  
    length = len(bin(number))-2
    for i in range(1,number+1):
        dec = str(i)
        octal = oct(i).lstrip("0o")
        hexal = hex(i).lstrip("0x").upper()
        binary = bin(i).lstrip("0b")
        print(dec.rjust(length),octal.rjust(length),hexal.rjust(length),binary.rjust(length))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)