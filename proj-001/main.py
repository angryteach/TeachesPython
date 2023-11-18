#
# This programme computes the area of a right-angled triangle
#


# the entry point
def main():
    n = 3
    while n > 0:
        n = n - 1
        get_user_input()
        if a == "x" or b == "x":
            print("You have used the escape key 'x' to exit the programme.")
            break
        check_user_input()
        calc()

def get_user_input():
    # Get user input
    print("Let's calculate the area of a right triangle. If you wish to exit, enter x during input.")
    global a
    global b
    a = input("What's the length of one side? ")
    b = input("What's the length of the other side? ")

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

