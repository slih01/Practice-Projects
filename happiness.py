# Simple programme that adds 1 to happiness for each member of set A in
# array N and takes off 1 for each B in N

print("Hi. Please enter inputs when asked. Please note that the size of the sets "
      "should not be bigger that 10 and the positive integers within the sets "
      "should not be higher than 100 ")

# Requests from user number of integers for set n and m.
while True:
    try:
        n, m = map(int, input("Enter the number of integers you want in set N, "
                              "and number of integers in sets A & B separated by "
                              "a space: ").split())
        inputs = [n, m]
    except ValueError:
        print("Sorry you have not entered two integers separated by a space")
    else:
        if not all(1 <= i <= 10 for i in inputs):
            print("Sorry your numbers are not within range from 1-10")
        else:
            break

# Ask for integer input for set N and checks it is correct length
while True:
    try:
        set_n = list(map(int, input("Enter {} integers for set N: ".format(n)).split()))
    except ValueError:
        print("Sorry you have not entered integers")
    else:
        if len(set_n) != n:
            print("Sorry you need to enter {} integers".format(n))
        elif not all(1 <= i <= 100 for i in set_n):
            print("Sorry, you have entered numbers outside of range 1-100")
        else:
            break

# Ask for integer input for set A and checks it is correct length
while True:
    try:
        set_a = list(map(int, set(input("Enter {} unique integers for set A: "
                                        .format(m)).split())))
    except ValueError:
        print("Sorry you have not entered integers")
    else:
        if len(set_a) != m:
            print("Sorry you need to enter {} unique integers".format(m))
        elif not all(1 <= i <= 100 for i in set_a):
            print("Sorry, you have entered numbers outside of range 1-100")
        else:
            break

# Ask for integer input for set B and checks it is correct length
while True:
    try:
        set_b = list(map(int, set(input("Enter {} unique integers for set B: "
                                        .format(m)).split())))
    except ValueError:
        print("Sorry you have not entered integers")
    else:
        if len(set_b) != m:
            print("Sorry you need to enter {} unique integers".format(m))
        elif not all(1 <= i <= 100 for i in set_b):
            print("Sorry, you have entered numbers outside of range 1-100")
        else:
            break

# Checks if and member of A is in N and adds one to happiness if so, and takes
# off one if B is in N
happiness = sum([(i in set_a) - (i in set_b) for i in set_n])

print(happiness)
