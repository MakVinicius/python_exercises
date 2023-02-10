def number_length(num, len=0):
    if num < 10:
        return len + 1
    else:
        return number_length(num/10, len+1)

print(number_length(1000))