def primer(b = 1):
    """
    Returns all integer values within two numbers. When it is not stated gives values from 1.
    """
    try:
        n = int(input(f"Enter a value (n) to display prime numbers between {b} and 'n': "))
        prime_list = []
        if b >= n:
            print(f"Inapplicable demand. Defined range is {b} - {n}.")
        elif b == 1:
            for i in range(2, n):
                for j in range (2, i + 1):
                    if i % j == 0 and i != 2:
                        break
                    elif i == j + 1 and i % j != 0 or i == 2:
                        prime_list.append(i)
        else:
            for i in range(2, n):
                for j in range (b, i + 1):
                    if i % j == 0 and i != 2:
                        break
                    elif i == j + 1 and i % j != 0 or i == 2:
                        prime_list.append(i)
         
        return prime_list
    except:
        print("Please enter a valid integer number")
