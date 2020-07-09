try:
    number_given = int(input("Number: ")) 
    for i in range(1,number_given):
        remainder = number_given % i
        if i != 1 and remainder == 0:
            print(f"{number_given} is NOT a prime number")
            break
        if i == (number_given - 1) and remainder != 0:
            print(f"{number_given} is a prime number")
except:
    print("Please enter a valid integer number")
