def is_safe(level):
    """
    :param level: list of nums to check
    :return int: 0 = not safe | 1 = safe
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

def problem_solver(level):
    """
    Try to solve bad levels by removing 1 item at a time and re-checking

    :param level: list of nums to check
    :return int: 0 = not safe | 1 = safe
    """
    chk = 0
    for i in range(0, len(level)):
        tmp = level.copy()
        del(tmp[i])
        chk = is_safe(tmp)
        if chk == 1:
            return chk
    return chk


safety = []
with open("day2\input_day2") as file:
    while line := file.readline().rstrip():
        level = line.split()
        chk = is_safe(level)
        if chk == 0:
            chk = problem_solver(level)
        safety.append(chk)
z = 0
for i in safety:
    z += i
#print(safety)
print(z)