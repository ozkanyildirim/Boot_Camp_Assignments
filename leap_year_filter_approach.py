def leap_detector():
    '''
    Checks if a given year is LEAP year (when input is just a year) or all leap years in a time interval (input cinsist of two years).
    '''
    try:
        years = input('Enter a year interval to see all leap years within or \n enter just a year to see if it is a leap year or not : ').split()
        start = int(years[0])
        if len(years) > 1 : 
            stop = int(years[1])
            year_lst = list(range(start, stop))
            print(f'Leap years between {start} - {stop} years : {list(filter((lambda x : x % 4 == 0 and x % 100 != 0 or x % 400 == 0), year_lst))}')
        else:
            if start % 4 == 0 and start % 100 != 0 or start % 400 == 0 :
                print(f'{start} is a leap year')
            else:
                print(f'{start} is NOT a leap year')
                
    except:
        print(f'{years} is not valid. Please enter a valid year or year interval')

leap_detector()
        
        
                  
