import time



def clock_test():
    print(f"Hello from exp-calculator!\nToday is {time.strftime('%A %B %d %Y', time.localtime())} and the time is {time.strftime('%H:%M')}.\nLet's do some calculating!")

    start_time = time.time()
    current_time = start_time
    test_clock = 3
    print(f"Testing seconds-clock for {test_clock} seconds\nStart time is: {time.strftime('%H:%M:%S', time.localtime(start_time))}\nRunning...")
    

    while test_clock > -1:
        current_time = time.time()
        test_clock -= 1
        time.sleep(1)

    print(f"Start time was {time.strftime('%H:%M:%S', time.localtime(start_time))} and current time is: {time.strftime('%H:%M:%S', time.localtime())}\nTest ran for {(current_time - start_time)} seconds.")