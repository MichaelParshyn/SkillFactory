import numpy as np

lower_limit=1
upper_limit=100
low=lower_limit
up=upper_limit
number=0

def play_game():
    """
    Automatically plays "guess_number" game 100 times. It is not recommemded to increase times because of the limitation of the maximum recursion depth .
    """
    global number
    times_to_win=[]
    np.random.seed(1)
    rand_array=np.random.randint(1,101, size=(100)) 

    for item in rand_array:
        number=np.random.randint(lower_limit,upper_limit+1)
        times_to_win.append(guess_number(predict=(low+up)//2))      
    result=int(np.mean(times_to_win))
    return result

def guess_number(predict, low=low, up=up, tries=0):  
    """
    The game that is trying to guess number using the most optimal algorithm.
    """
    predict=(low+up)//2       
    if number==predict:
        print(f'Number: {number}; tries: {tries+1}')
        return tries+1             
    elif number>predict: return guess_number((low+up)//2, predict, up, tries=tries+1)        
    elif number<predict: return guess_number((low+up)//2, low, predict, tries=tries+1)   

print(play_game())