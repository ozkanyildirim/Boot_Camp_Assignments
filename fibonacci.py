def fibonacci_tree(n):
    """
    Gives first n Fibonacci numbers as a set.
    """
    fibonacci = [1, 1]
    for i in range(2, n):
        sum_list = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(sum_list)
    return fibonacci

print(fibonacci_tree(int(input('Fibonacci numbers smaller than or equal: '))))

