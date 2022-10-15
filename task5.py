n = int(input())
pupils = dict()
mark = 3
marks = [0] * mark
for _ in range(n):
    pupil = input().split()
    last_name = pupil[0]
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    for i in range(mark):
        marks[i] += pupils[last_name][i]

print('-' * 20)
avg_marks = (str('%.2f' % (marks[i]/n)) for i in range(mark))
print(' '.join(avg_marks))
