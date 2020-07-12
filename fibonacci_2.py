def fibonacci_till(n):    
    """
    Gives Fibonacci numbers till a given number.
    """
    
    fibonacci = [1, 1]
    while fibonacci[-1] + fibonacci[-2]  <= n: 
            sum_list = fibonacci[-2] + fibonacci[-1]
            fibonacci.append(sum_list)
    return fibonacci

print(fibonacci_till(55))
