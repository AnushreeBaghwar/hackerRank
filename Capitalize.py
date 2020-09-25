# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Complete the solve function below.
def solve(s):
    name = s.split()
    for i in name:
        s = s.replace(i,i.capitalize())
    return s    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
