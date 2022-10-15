n = int(input())
pupils = {}
mark = 3
output = []

for _ in range(n):
    pupil = input().split()
    last_name = pupil[0]
    pupils[last_name] = [int(i) for i in pupil[1:]]
    avg_mark = sum(pupils[pupil[0]])/mark
    output.append('%s %.2f' % (last_name, avg_mark))

print('-' * 20)
print('\n'.join(output))
