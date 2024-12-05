def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    :param n: The number to check.
    :param low: The lower bound (inclusive).
    :param high: The upper bound (inclusive).
    :return: True if n is within range, otherwise False.
    """
    return low <= n <= high
def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    print(f"Is {n} in the range [{low}, {high}]? {in_range(n, low, high)}")

if __name__ == "__main__":
    main()
