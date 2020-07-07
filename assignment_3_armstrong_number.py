given_number = input("Enter a positive number to see if it's an Armstrong one: ")
given_list = list(given_number)
given_set = set(given_number.lower())
number_set = set("0123456789")
decimal_set = set(",.")
negativity_set = set("-")
alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
sum_up = 0
if given_set & number_set == given_set:
    for i in given_list:
        sum_up += int(i) ** len(given_number)
    if sum_up == int(given_number):
        print(f"{given_number} is an Armstrong number")
    else:
        print(f"{given_number} is not an Armstrong number")
elif (given_set & (number_set | decimal_set)) == given_set:
    print("Please enter an integer number")
elif (given_set & (number_set | negativity_set) == given_set) and given_list[0] == "-":
    print("Please enter a positive number")
else:
    print("Do not use any entries other than numeric values")
