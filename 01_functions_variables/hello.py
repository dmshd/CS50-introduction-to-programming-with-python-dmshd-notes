def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", name)


main()


# Ask user for their name
# name = input("What's your name? ").strip().title()

# Remove whitespace from str
#name = name.strip()

# Capitalize user's name
#name = name.capitalize()

# Capitalize user's name
#name = name.title()

# remove whitespace from str and capitalize user's name
#name = name.strip().title()

# Split user's name into first name and last name
# first, last = name.split(" ")

# print(f"first: {first}, last: {last}")
# print(type(first))

# Say hello to user
# print(f"hello", name)
# print(f"hello", end="???")
# print(name)
# print(f"hello", name)

def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
