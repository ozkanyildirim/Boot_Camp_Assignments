def fizzbuzz(b = 1):
    """
    if a number is multiple of 3, prints "Fizz" instead of this number,
if a number is multiple of 5, prints "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, prints "FizzBuzz",
print the rest of the numbers unchanged. 
    """
    try:
        n = int(input(f"Enter a value (n) to display FizzBuzz numbers between {b} and 'n': "))
        prime_list = []
        
        if b >= n:
            print(f"Inapplicable demand. Defined range is {b} - {n}.")
        demanded_list = list(range(b, n))
        fizzy_buzzy = lambda x : 'FizzBuzz' if x % 15 == 0 else('Fizz' if x % 3 == 0 else ('Buzz' if x % 5 == 0 else x))

        return print(list((map(fizzy_buzzy, demanded_list)))) 
    except:
        print("Please enter a valid integer number")
