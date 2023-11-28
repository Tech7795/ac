#@title q8) Displaying the pattern of pyramid
def print_combined_triangle(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Example usage:
n = int(input("enter the no.of rows needed for semi pyramid:"))
print_combined_triangle(n)
