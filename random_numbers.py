import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    # Call the append_random_numbers function to
    # add one random number to the numbers list.
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # Call the append_random_numbers function to add
    # three random numbers to the numbers list.
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")


def append_random_numbers(numbers_list,quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for _ in range(quantity):
        add = random.uniform(0,100)
        numbers_list.append(round(add,1))



if __name__ == "__main__":
    main()