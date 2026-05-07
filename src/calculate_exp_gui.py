import time




def start_exp(start_lvl, start_exp):
    try:
        if int(start_lvl) < 1:
            return 'Level must be more than 0'
    except ValueError:
        return 'Level must be whole numbers'

    try:
        start_exp = start_exp.replace(',', '.', 1)
        if float(start_exp) >= 100.00:
            return 'Percentage must be less than 100'
    except ValueError:
        return 'Exp % must be numbers with fraction'
            
    start_dir = {
        'time': time.localtime(),
        'level': int(start_lvl),
        'exp': round(float(start_exp), 2)
    }
    return start_dir

def end_exp(start, end_lvl, end_exp):
    level = True
    while level:
        try:
            if end_lvl < start['level']:
                print("Level must be more or equal to starting level")
            else:
                level = False
        except ValueError:
            print('Input must be whole numbers or "exit"')
    exp = True
    while exp:
        try:
            if end_exp >= 100.00:
                print("Percentage must be less than 100")
            else:
                exp = False
        except ValueError:
            print('Input must be numbers or "exit"')

    end = {
        'time': time.localtime(),
        'level': end_lvl,
        'exp': end_exp
    }
    return (start, end)


def calculate_exp(input): #input is a tuple of the start and end dictionaries, keys = time, level, exp
    start = input[0]
    end = input[1]
    print(f"==========\nYou started the grind at {time.strftime('%H:%M', start['time'])} with lvl {start['level']} and {round(start['exp'], 2)}% and ended at {time.strftime('%H:%M', end['time'])} with lvl {end['level']} and {round(end['exp'], 2)}%")
    gained_levels = end['level'] - start['level']
    if gained_levels > 0 and end['exp'] < start['exp']:
        gained_levels -= 1
        end['exp'] += 100
    gained_exp = end['exp'] - start['exp']
    seconds_spent = time.mktime(end['time']) - time.mktime(start['time'])
    print(f"You gained {gained_levels} and {round(gained_exp, 2)}% in {round(seconds_spent/60, 2)} minutes")
    exp_per_second = ((gained_exp + (100 *gained_levels)) / seconds_spent) 
    next_level = time.time() + ((100 - end['exp']) / exp_per_second)
    extra_msg = ""
    if exp_per_second > 1000/3600:
        extra_msg = "\n- That's a lot... You must be on a private server..."
    elif exp_per_second < 1/3600:
        extra_msg =  "\n- Wow... are you even trying?"
    
    print(f"This results in {round(exp_per_second * 3600, 2)}% per hour and your next level up should be at {time.strftime('%H:%M', time.localtime(next_level))}" + extra_msg + "\n")
    time.sleep(2)
    print("=========\nNew calculation")