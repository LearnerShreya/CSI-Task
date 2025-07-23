# Print the Triangle pattern
# Create lower triangular, upper triangular and pyramid containing the "*" character.



class TrianglePatterns:
    """
    Generates various star patterns including triangles and pyramids.
    Call show_all_patterns(n) to display all at once, or call individually.
    """

    @staticmethod
    def _print_line(spaces, stars):
        print("  " * spaces + "* " * stars)

    @staticmethod
    def left_lower_triangle(n):
        for i in range(1, n + 1):
            TrianglePatterns._print_line(0, i)

    @staticmethod
    def right_lower_triangle(n):
        for i in range(1, n + 1):
            TrianglePatterns._print_line(n - i, i)

    @staticmethod
    def left_upper_triangle(n):
        for i in range(n, 0, -1):
            TrianglePatterns._print_line(0, i)

    @staticmethod
    def right_upper_triangle(n):
        for i in range(n):
            TrianglePatterns._print_line(i, n - i)

    @staticmethod
    def full_pyramid(n):
        for i in range(1, n + 1):
            TrianglePatterns._print_line(n - i, 2 * i - 1)

    @staticmethod
    def inverted_pyramid(n):
        for i in range(n, 0, -1):
            TrianglePatterns._print_line(n - i, 2 * i - 1)

    @classmethod
    def show_all_patterns(cls, n):
        patterns = [
            ("Left Lower Triangle", cls.left_lower_triangle),
            ("Right Lower Triangle", cls.right_lower_triangle),
            ("Left Upper Triangle", cls.left_upper_triangle),
            ("Right Upper Triangle", cls.right_upper_triangle),
            ("Full Pyramid", cls.full_pyramid),
            ("Inverted Pyramid", cls.inverted_pyramid),
        ]
        for title, func in patterns:
            print(f"\n{title}:")
            func(n)

# Run code
if __name__ == "__main__":
    size = int(input("Enter size of pattern: "))
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
