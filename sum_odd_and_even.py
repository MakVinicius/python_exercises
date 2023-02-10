def sum_odd_and_even(lst):
    sum_even =0
    sum_odd = 0
    for i in lst:
        if i % 2 == 0:
            sum_even += i
        elif i % 2 != 0:
            sum_odd += i
    
    return [sum_even, sum_odd]

print(sum_odd_and_even([0, 0]))