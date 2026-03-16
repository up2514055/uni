from math import sqrt

def sum_of_list(numbers, length):
    total = 0
    if length == 0:
        return 0
    else:
        for i in range(length):
            number = float(numbers[i])
            total += number
        return total


def process_list(numbers):
    total = sum_of_list(numbers, 5)
    return sqrt(total)


def main():
    data = {
        1: [48.13, 17.87, 45.52, -39.44, 16.84, -15.94, 34.27, 41.43],
        2: [-31.12, 25.54, 5.11, -39.51, -22.14, 98.32, 41.31],
        3: [39.58, -12.6, -24.37, -28.54, 14.64],
        4: [-32.27, 22.0, -11.61, 42.83, -46.75, 48.62],
        5: [-43.82, -42.23, 43.06, 3.18, -12.98, 20.48],
    }

    for key, value in data.items():
        print(f"List {key} has the following numbers: {value}")
        try:
            result = process_list(value)
            print(f"The processed value of this list is {result}")
        except ValueError:
            print(f"Cannot calculate square root of a negative total in list {key}. ")



main()