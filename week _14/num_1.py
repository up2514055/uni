def sum_list(numbers, count):
    total = 0
    for i in range(count):
        total += numbers[i]
    return total


def get_number():
    number = int(input("Enter a number: "))
    return number


def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = get_number()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = get_number()
        if count >= 0:
            total = sum_list(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")
        else:
            break


main()