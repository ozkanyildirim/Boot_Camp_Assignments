import csv
def character_populater():
    '''
    Receives a sentence as an imput or a .txt or .csv file to populate all characters within a dictionary.
    '''
    try:
        sentence = input('Enter a text or \n enter a file name : ')
        
        def populate(x):
            character_set = set(x)
            character_list = list(x)
            populator = {}
            for i in character_set:
                populator[i] = character_list.count(i)
            population_sorted = {k: v for k, v in sorted(populator.items(), reverse = True, key=lambda item: item[1])}
            print(population_sorted)
            
        if len(sentence.split()) ==1 and sentence[-4:] == '.txt':
            with open(sentence, 'r', encoding = 'utf-8') as file:
                interior = file.read()
                populate(interior)                
            
        elif len(sentence.split()) ==1 and sentence[-4:] == '.csv' :
            with open(sentence, 'r', newline = '', encoding = 'utf-8') as file:
                csv_rows = csv.reader(file, delimiter= ",") 
                interior = file.read()
                populate(interior)
                populate(csv_rows)
                                   
        else:
            populate(sentence)          
                
    except:
        print(f'Unable to open file, please check if the file is in the right directory.')

character_populater()
