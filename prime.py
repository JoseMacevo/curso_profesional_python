def is_prime(number: int) -> bool:
    """
    Returns True if mumber is prime or false if not
    """

    result_list = [x for x in range(2, number) if number % x == 0]
    return len(result_list) == 0


def main():
    number = int(input("Insert a whole number please: "))
    if is_prime(number):
        print(f"The number {number} is a prime number")
    else:
        print(f"The number {number} isn't a prime number")


if __name__ == '__main__':
    main()
