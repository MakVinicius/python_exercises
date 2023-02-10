def total_overs(balls):
    overs = round(balls / 6, 0)
    balls_left = balls % 6
    result = float(str(int(overs)) + "." + str(int(balls_left)))
    return result

print(total_overs(0))