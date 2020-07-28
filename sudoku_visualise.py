def sudoku_display_unit(sudoku):
    '''
    Reshapes a given array inorer to get a predefined display format of SUDOKU. 
    No matter what the input size output will be in the predefined format. 
    
    '''
    count = 0 
    for i in sudoku:
        if count % 3 == 0:
            print(*'-'*(len(i) + int((len(i) / 3)-1)))
        
        for j in range(len(i)):
                if j == (len(i)-3):
                    print(*i[-3:])
                elif j % 3 == 0:
                    print(*i[j:j + 3], '|', end=' ')
        count += 1
    print(*'-'*(len(i) + int((len(i) / 3)-1)))
