# import the time module 
import time 

from playsound import playsound

def pom(t):
    while t:
        #divmod for minutes and seconds ###divmod(quotient, remainder)
        mins, secs = divmod(t, 60)
        #string formatting
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print the timer and use '\r' to reset (erase and reprint new timer values)
        print(timer, end="\r")
        #.sleep to make code wait for one second
        time.sleep(1)
        #decrement time
        t -= 1

for i in range(4):
    print('\n')
    print('Work for 25 minutes <3')
    playsound('work_time_start.wav')

    t = 1500
    pom(int(t))

    print('\n')
    print('Take a break for 5 minutes <3')
    playsound('break_time_start.wav')
    t = 300 
    pom(t)

print('\n')
print('Take a long break, then re-run the program <3')
playsound('long_break_time_start.wav')