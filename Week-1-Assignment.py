# Print the Triangle pattern
# Create lower triangular, upper triangular and pyramid containing the "*" character.

def left_lower_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

def right_lower_triangle(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)

def left_upper_triangle(n):
    for i in range(n):
        print("* " * (n - i))

def right_upper_triangle(n):
    for i in range(n):
        print("  " * i + "* " * (n - i))

def full_pyramid(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * (2 * i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * (2 * i - 1))

def show_all_patterns(n):
    print("\nLeft Lower Triangle:")
    left_lower_triangle(n)

    print("\nRight Lower Triangle:")
    right_lower_triangle(n)

    print("\nLeft Upper Triangle:")
    left_upper_triangle(n)

    print("\nRight Upper Triangle:")
    right_upper_triangle(n)

    print("\nFull Pyramid:")
    full_pyramid(n)

    print("\nInverted Pyramid:")
    inverted_pyramid(n)

if __name__ == "__main__":
    size = int(input("Enter the size of the pattern: "))
    show_all_patterns(size)


    
# OUTPUT:

# Enter the size of the pattern: 5

# Left Lower Triangle:
# * 
# * * 
# * * *
# * * * *
# * * * * *

# Right Lower Triangle:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# Left Upper Triangle:
# * * * * *
# * * * *
# * * *
# * *
# *

# Right Upper Triangle:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# Full Pyramid:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# Inverted Pyramid:
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
