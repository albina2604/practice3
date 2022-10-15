n = int(input())
p = [int(s) for s in input().split()]
m = int(input())
q = [int(s) for s in input().split()]

length_r = max(n, m) + 1
r = [0]*length_r
for i in range(length_r):
    r[i] = (p[i] if i <= n else 0)+(q[i] if i <= m else 0)
while length_r > 0 and r[length_r-1] == 0:
    length_r -= 1
if length_r == 0:
    print(0)
else:
    print(*r[:length_r])
