numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_ = sum(numbers[0:4])+sum(numbers[5:])
len_ = len(numbers)
average = sum_ / len_

numbers[4] = average

print("Измененный список:",numbers)
