name = input("What is your name? ")
age = int(input("{}, How are you old? ".format(name)))

if 18 <= age < 31:
    print("You can go to a \"18-30 Holidays\", {}".format(name))
else:
    print("Sorry, you must be 18-30 yo")
