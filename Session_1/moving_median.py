import statistics

def moving_median(data):
    current_list = []
    for num in data:
        current_list.append(num)
        current_list.sort()
        yield statistics.median(current_list)

numbers = [2, 5, 1, 8, 3, 9]
for median in moving_median(numbers):
    print(median)