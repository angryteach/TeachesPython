#
# This programme computes the area of a right-angled triangle
#

import sys

# the entry point
def main():
    try:
        print("Let's calculate the area of a right triangle. \nIf you wish to exit, enter x during input or press Ctrl-c.\n\n")
        get_user_input()
    except KeyboardInterrupt:
        print("\nYou interrupted the programme with Ctrl-c.")


def get_user_input():
    # Get user input
    try:
        counter = int(input("How many calculations do you require? "))
        while counter > 0:
            a = input("\nWhat's the length of one side? ")
            if a == "x":
                print("\nYou have used the escape key 'x' to exit the programme.")
                break
            b = input("\nWhat's the length of the other side? ")
            if b == "x":
                print("\nYou have used the escape key 'x' to exit the programme.")
                break
            calc(*check_user_input(a, b))
            counter -= 1
    except ValueError:
        print("\n\nYou should enter an integer")
        get_user_input()
    except TypeError: # raised if a non-integer is used
        pass # does not pass the error to calc() so that check_user_input() can handle non-numbers

# Check whether user gives numbers
def check_user_input(a, b):
    try:
        a = float(a)
        b = float(b)
        return a, b
    except ValueError:
        print("!!!One or more numbers you gave me were not numbers!!!")


# Do the calculation
def calc(a, b):
    area = 0.5 * a * b # no need to use try-except because get_user_input() deals with TypeError
    print("The area is ", area)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            calc(*check_user_input(*sys.argv[1:]))
        except TypeError:
            print("Exited.")
    else:
        main()
