def fizzbuzz(b = 1):
    """
    if a number is multiple of 3, prints "Fizz" instead of this number,
if a number is multiple of 5, prints "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, prints "FizzBuzz",
print the rest of the numbers unchanged. 
    """
    try:
        n = int(input(f"Enter a value (n) to display FizzBuzz numbers between {b} and 'n': "))
        fizz_buzz = []
        
        if b >= n:
            print(f"Inapplicable demand. Defined range is {b} - {n}.")
        for i in range(b, n):
            if i % 15 == 0:
                fizz_buzz.append('FizzBuzz')
            elif i % 3 == 0:
                fizz_buzz.append('Fizz')
            elif i % 5 == 0:
                fizz_buzz.append('Buzz')
            else:
                fizz_buzz.append(i)

        return fizz_buzz
    except:
        print("Please enter a valid integer number")
