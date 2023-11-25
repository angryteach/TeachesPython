#
# This programme computes the area of a right-angled triangle
#

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
            global a
            global b
            a = input("\nWhat's the length of one side? ")
            if a == "x":
                print("\nYou have used the escape key 'x' to exit the programme.")
                break
            b = input("\nWhat's the length of the other side? ")
            if b == "x":
                print("\nYou have used the escape key 'x' to exit the programme.")
                break
            check_user_input()
            calc()
            counter -= 1
    except ValueError:
        print("\n\nYou should enter an integer")
        get_user_input()

# Check whether user gives numbers
def check_user_input():
    try:
        global a
        global b
        a = float(a)
        b = float(b)
    except ValueError:
        print("!!!One or more numbers you gave me were not numbers!!!")


# Do the calculation
def calc():
    try:
        global a
        global b
        area = 0.5 * a * b
        print("The area is ", area)
    except TypeError:
        print("!!!Nothing to calculate. An error must have occured.!!!")




if __name__ == "__main__":
    main()

