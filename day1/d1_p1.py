first = []
second = []
ans = []
with open("day1\input_day1") as file:
    while line := file.readline():
        newline = line.rstrip().split(' ')
        first.append(int(newline[0]))
        second.append(int(newline[len(newline)-1]))
    first.sort()
    second.sort()
    for i in range(0, len(first)):
        x = abs(int(first[i]) - int(second[i]))
        ans.append(x)

z = 0
for i in ans:
    z += i
print(ans)
print(z)