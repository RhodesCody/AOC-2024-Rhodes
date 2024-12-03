import re

def mult(list):
    """
    :param list: list of num pairs to multiply
    :return int: result of adding up all mult pairs
    """
    ans = 0
    for i in list:
        x = int(i[0]) * int(i[1])
        ans += x
    return ans

z = 0

with open("day3\input_day3.txt") as file:
    while line := file.readline().rstrip():
        match2 = re.findall(r'mul\((-?\d+),(-?\d+)\)', line)
        z += mult(match2)

print(z)