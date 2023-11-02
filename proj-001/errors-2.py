import keyword

def main():
    calc
    outpot()

 def calc()
    try:
        global a
	a = input()
    except ValueError:
       print("You should use numbers only!")

def output():
   try:
     print("The square of {0} is {1}".format(a, a*a))
    except UnboundLocalError:
        print("Got an error.)

if __name__ == __main__:
    main()
