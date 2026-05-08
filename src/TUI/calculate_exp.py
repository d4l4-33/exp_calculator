import time
import sys


def take_input(text):
    user_input = input(text)
    if user_input == "exit" or user_input == "Exit":
        sys.exit(0)
    return user_input


def start_exp():
    level = True
    while level:
        try:
            start_level = int(take_input("Starting level: "))
            if start_level < 1:
                print("Level must be more than 0")
            else:
                level = False
        except ValueError:
            print('Input must be whole numbers or "exit"')
    exp = True
    while exp:
        try:
            start_exp = float(take_input("Starting exp %: "))
            if start_exp >= 100.00:
                print('Percentage must be less than 100')
            else:
                exp = False
        except ValueError:
            print('Input must be numbers or "exit"')
        
    print(f"Your starting level and exp at {time.strftime('%H:%M')} is: lvl {start_level} at {round(start_exp, 2)}%. Get grinding!\n=====")
    start = {
        'time': time.localtime(),
        'level': start_level,
        'exp': start_exp
    }
    return start

def end_exp(start):
    level = True
    while level:
        try:
            end_level = int(take_input("End level: "))
            if end_level < start['level']:
                print("Level must be more or equal to starting level")
            else:
                level = False
        except ValueError:
            print('Input must be whole numbers or "exit"')
    exp = True
    while exp:
        try:
            end_exp = float(take_input("End exp %: "))
            if end_exp >= 100.00:
                print("Percentage must be less than 100")
            else:
                exp = False
        except ValueError:
            print('Input must be numbers or "exit"')

    end = {
        'time': time.localtime(),
        'level': end_level,
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
    print("=========\nNew calculation\nTo exit type 'exit'")