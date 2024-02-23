# A simple dead man's switch code
# Very basic structure coded, intended for user customization

import time
import threading

hour = 3600 # seconds
limit = hour/2
Condition = False
Run = True

def Switch_Case():
    # Switch code execution where if you fail to reach out to your terminal with input.
    print("code")

def Check():
    global Condition, Run
    start_time = time.time()

    while True:
        stop_time = time.time()
        if int(stop_time-start_time) == limit:
            Switch_Case()
            Run = False
            break
        
        if Condition:
            start_time = time.time()
            Condition = False

def main():
    global Condition
    while Run:
        raw = str(input(""))
        Condition = True

Thread1 = threading.Thread(target=Check)
Thread1.start()

main()



