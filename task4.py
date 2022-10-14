n = int(input())
pupils = dict()
mark = 3
for _ in range(n):
    pupil = [str(s) for s in input().split()]
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    print(f'{pupil[0]} {sum(pupils[pupil[0]])/mark:.2f}')
