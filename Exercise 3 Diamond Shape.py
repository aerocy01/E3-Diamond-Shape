def print_diamond(n):
    # Check if n is odd
    if n % 2 == 0:
        return "Please provide an odd integer."

    # Calculate the middle point
    mid = n // 2

    # Generate the upper part of the diamond
    for i in range(mid + 1):
        print(" " * (mid - i) + "*" * (2 * i + 1))

    # Generate the lower part of the diamond
    for i in range(mid - 1, -1, -1):
        print(" " * (mid - i) + "*" * (2 * i + 1))


n = int(input("Enter an odd integer: "))
result = print_diamond(n)
if result:
    print(result)
