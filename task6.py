n = int(input())
pupils = []
mark = 3
for _ in range(n):
    pupil = input().split()
    pupil[1:] = [int(i) for i in pupil[1:]]
    pupil.insert(0, -sum(pupil[1:])/mark)
    pupils.append(pupil)
print('-' * 20)
pupils.sort()
for pupil in pupils:
    print(
        pupil[1],
        ' '.join(str(mark) for mark in pupil[2:]),
        f'{-pupil[0]:.2f}'
    )
