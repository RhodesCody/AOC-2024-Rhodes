def is_safe(level):
    """
    Now with added problem solver capability!

    :param level: list of nums to check
    :return int: 0 = not safe | 1 = safe
    """
    tmp = []
    cnt_pos = 0
    cnt_neg = 0
    grace = True
    rt = 0
    for i in range(0, len(level)-1):
            x = int(level[i]) - int(level[i+1])
            if (x > 0):
                cnt_pos += 1
            if (x < 0):
                cnt_neg += 1
            
            y = -1
            if (i+2) <= len(level)-1:
                y = int(level[i]) - int(level[i+2])
            
            if abs(x) > 3:
                if grace and abs(y) <= 3:
                    rt = 1
                    grace = False
                else: 
                    return 0
            if abs(x) == 0:
                if abs(y) != 0 and grace:
                    rt = 1
                    grace = False
                else:
                    return 0
            tmp.append(x)

    if cnt_neg > 0 and cnt_pos <= 1 and grace:
        rt = 1
    elif cnt_pos > 0 and cnt_neg <= 1 and grace:
        rt = 1
    
    return rt

safety = []
with open("day2\input_day2") as file:
    while line := file.readline().rstrip():
        level = line.split()
        safety.append(is_safe(level))
z = 0
for i in safety:
    z += i
print(safety)
print(z)