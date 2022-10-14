n = int(input())
pupils = dict()
mark = 3
marks = [0 for i in range(mark)]
for _ in range(n):
    pupil = [str(s) for s in input().split()]
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    for i in range(mark):
        marks[i] += pupils[pupil[0]][i]
for i in range(mark):
    print(f'{marks[i]/n:.2f}')
