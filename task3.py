n = int(input())
a = [int(s) for s in input().split()]
p = int(input())
a.pop(p-1)

Q, K = [int(s) for s in input().split()]
a.insert(Q-1, K)

print(' '.join([str(i) for i in a]))
