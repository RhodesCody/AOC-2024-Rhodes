import re

def mult(list):
    """
    :param list: list of num pairs to multiply
    :return int: result of adding up all mult pairs
    """
    ans = 0
    do = True
    for i in list:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        else:
            if do:
                tmp = i[4:len(i)-1].split(',')

                ans += int(tmp[0]) * int(tmp[1])
    
    return ans


#
# Main
#
z = 0

with open("day3\input_day3.txt") as file:
    while line := file.readline().rstrip():
        pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        match2 = re.findall(pattern, line)
        z += mult(match2)

print(z)