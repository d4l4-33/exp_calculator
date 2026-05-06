import os
from clock_test import clock_test
from calculate_exp import *



def main():
    print(f'===== Welcome to the exp_calculator by d4l4-33 =====\nTo exit type "exit"\n')
    run = True
    while run:
        calculate_exp(end_exp(start_exp()))


if __name__ == "__main__":
    main()
