n = int(input())
pupils = []
mark = 3
for _ in range(n):
    pupil = [str(s) for s in input().split()]
    pupil[1:] = [int(i) for i in pupil[1:]]
    pupil.append(sum(pupil[1:])/mark)
    pupils.insert(0, pupil)

pupils_sorted = sorted(pupils)
print(pupils_sorted)
