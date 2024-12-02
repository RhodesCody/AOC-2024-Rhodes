first = []
second = []
ans = 0
z = 0
import os
cwd = os.getcwd()
with open("day1\input_day1") as file:
    while line := file.readline():
        newline = line.rstrip().split(' ')
        first.append(int(newline[0]))
        second.append(int(newline[len(newline)-1]))
    first.sort()
    second.sort()
    for i in first:
        ans += i * second.count(i)
print(ans)