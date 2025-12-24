def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print("Sum of digits:", result)
