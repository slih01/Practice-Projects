# Simple programme that adds 1 to happiness for each member of A in set N and takes one off for each B in N

# Requests from user number of integers for set n and m.
while True:
    try:
        a, b = input("Enter number of integers in set N, and number of integers "
                     "in sets A & B separated by a space: ").split()
    except ValueError:
        print("Sorry you have not entered two integers separated by a space")
    else:
        break

n = int(a)
m = int(b)
happiness = 0

# Ask for integer input for set N and checks it is correct length

while True:
    set_n = input("Enter {} integers for set N: ".format(n)).split()
    if len(set_n) != n:
        print("Sorry you need to enter {} integers".format(n))
    else:
        break

# Ask for integer input for set A and checks it is correct length
while True:
    set_a = input("Enter {} integers for set A: ".format(m)).split()
    if len(set_a) != m:
        print("Sorry you need to enter {} integers".format(m))
    else:
        break

# Ask for integer input for set B and checks it is correct length
while True:
    set_b = input("Now enter {} integers for set B: ".format(m)).split()
    if len(set_b) != m:
        print("Sorry you need to enter {} integers".format(m))
    else:
        break

# Checks if and member of A is in N and adds one to happiness if so, and takes off one if B is in N
for i in set_n:
    if i in set_a:
        happiness += 1
    if i in set_b:
        happiness -= 1

print(happiness)