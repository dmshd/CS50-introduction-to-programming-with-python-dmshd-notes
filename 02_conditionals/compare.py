x = int(input("What's x? "))
y = int(input("What's y? "))

"""
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# problem : we always ask three question no matter what the answer is
# solution : elif
"""


"""
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# it's gonna be mutually exclusive and it's gonna be executed only once
# if the first condition is true, it's gonna be executed and the rest of the code is gonna be skipped
# if the first condition is false, it's gonna go to the next condition and so on

# problem : what if we want to print something if none of the conditions are true?
# solution : else

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
"""

"""
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

"""
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


