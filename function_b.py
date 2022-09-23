# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 10001

    """
    input_int = True
    sum = 0

    while input_int != 0 and sum < 1000:
        input_int = int(input("Enter an integer:"))
        sum += input_int
        print(f'ongoing sum: {sum}')

    print(sum)
    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
