# Print the Triangle pattern
# Create lower triangular, upper triangular and pyramid containing the "*" character.


class TrianglePatterns:
    """
    Generates and prints various star (*) patterns including different triangles and pyramids.
    The size parameter controls the dimensions of the patterns.
    """

    @staticmethod
    def left_lower_triangle(n):
        for i in range(1, n + 1):
            print("* " * i)

    @staticmethod
    def right_lower_triangle(n):
        for i in range(1, n + 1):
            print("  " * (n - i) + "* " * i)

    @staticmethod
    def left_upper_triangle(n):
        for i in range(n):
            print("* " * (n - i))

    @staticmethod
    def right_upper_triangle(n):
        for i in range(n):
            print("  " * i + "* " * (n - i))

    @staticmethod
    def full_pyramid(n):
        for i in range(1, n + 1):
            print("  " * (n - i) + "* " * (2 * i - 1))

    @staticmethod
    def inverted_pyramid(n):
        for i in range(n, 0, -1):
            print("  " * (n - i) + "* " * (2 * i - 1))

    @classmethod
    def show_all_patterns(cls, n):
        print("\nLeft Lower Triangle:")
        cls.left_lower_triangle(n)

        print("\nRight Lower Triangle:")
        cls.right_lower_triangle(n)

        print("\nLeft Upper Triangle:")
        cls.left_upper_triangle(n)

        print("\nRight Upper Triangle:")
        cls.right_upper_triangle(n)

        print("\nFull Pyramid:")
        cls.full_pyramid(n)

        print("\nInverted Pyramid:")
        cls.inverted_pyramid(n)


if __name__ == "__main__":
    size = int(input("Enter the size of the pattern: "))
    TrianglePatterns.show_all_patterns(size)


    
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
