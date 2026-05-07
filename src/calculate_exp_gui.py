import time




def start_exp(start_lvl, start_exp):
    try:
        if int(start_lvl) < 1:
            return 'Level must be more than 0'
    except ValueError:
        return 'Level must be whole numbers'

    try:
        start_exp = start_exp.replace(',', '.', 1).replace('%', '')

        if float(start_exp) >= 100.00:
            return 'Percentage must be less than 100'
    except ValueError:
        return 'Exp % must be numbers with or without decimal'
            
    start_dir = {
        'time': time.localtime(),
        'level': int(start_lvl),
        'exp': round(float(start_exp), 2)
    }
    return start_dir

def end_exp(start, end_lvl, end_exp):
    if len(start.keys()) == 0:
        return 'Start input required'
    try:
        if int(end_lvl) < start['level']:
            return "Ok... So you lost exp?"
    except ValueError:
        return 'Level must be whole numbers'

    try:
        end_exp = end_exp.replace(',', '.', 1).replace('%', '')
        if float(end_exp) >= 100.00:
            return 'Percentage must be less than 100'
    except ValueError:
        return 'Exp % must be numbers with or without decimal'
            
    end_dir = {
        'time': time.localtime(),
        'level': int(end_lvl),
        'exp': round(float(end_exp), 2)
    }
    return end_dir


def calculate_exp(start, end):
    calc_start = start
    calc_end = end
    gained_levels = calc_end['level'] - calc_start['level']
    if gained_levels > 0 and calc_end['exp'] < calc_start['exp']:
        gained_levels -= 1
        calc_end['exp'] += 100
    gained_exp = calc_end['exp'] - calc_start['exp']
    seconds_spent = time.mktime(calc_end['time']) - time.mktime(calc_start['time'])
    exp_per_second = ((gained_exp + (100 *gained_levels)) / seconds_spent) 
    next_level = time.time() + ((100 - calc_end['exp']) / exp_per_second)
    extra_msg = ""
    if exp_per_second > 1000/3600:
        extra_msg = "\n\nThat's a lot... You must be on a private server..."
    elif exp_per_second < 1/3600:
        extra_msg =  "\n\nWow... are you even trying?"
    
    return(f"You gained {gained_levels} and {round(gained_exp, 2)}% in {round(seconds_spent/60, 2)} minutes\nThis results in {round(exp_per_second * 3600, 2)}% per hour.\nYour next level up should be at {time.strftime('%H:%M', time.localtime(next_level))}" + extra_msg + "\n")
