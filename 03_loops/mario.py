# def main():
#     print("#")
#     print("#")
#     print("#")


def main():
    # print_column(3)
    # print_row(4)
    print_square(3)

# def print_square(size):
#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             print("#", end="")
#         print()

def print_square(size):
    for i in range(size):
        # print("#" * size)
        print_row(size)

def print_row(width):
    print("#" * width)

def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

main()
