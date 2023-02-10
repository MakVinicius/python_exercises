import math

def line_length(dot1, dot2):
    result = math.sqrt((dot1[0] - dot2[0]) * (dot1[0] - dot2[0]) + (dot1[1] - dot2[1]) * (dot1[1] - dot2[1]))
    return round(result, 2)

print(line_length([0, 0], [1, 1]))