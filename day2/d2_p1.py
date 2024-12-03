def is_safe(level):
    """
    :param level: list of nums to check
    :return: 0 = not safe | 1 = safe
    """
    tmp = []
    for i in range(0,len(level)-1):
            x = int(level[i]) - int(level[i+1])
            if abs(x) > 3:
                return 0
            if abs(x) == 0:
                return 0
            tmp.append(x)
    if (all(int(num) < 0 for num in tmp)):
        return 1
    if (all(int(num) > 0 for num in tmp)):
        return 1
    return 0

safety = []
with open("day2\input_day2") as file:
    while line := file.readline().rstrip():
        level = line.split()
        safety.append(is_safe(level))
z = 0
for i in safety:
    z += i
print(z)