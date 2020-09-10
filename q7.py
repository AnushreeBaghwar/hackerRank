# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_int = set(map(int,input().split()))
n = int(input())
n_int = set(map(int,input().split()))
diff1 = m_int.difference(n_int)
diff2 = n_int.difference(m_int)
diff_join = diff1.union(diff2)
sym_diff = sorted(list(diff_join))
for i in sym_diff:
    print(i)

