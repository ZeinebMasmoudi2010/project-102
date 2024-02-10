import time

seconds=int(input("Enter the time and number of seconds: "))

def countdown(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)

        if mins<10:
            mins=f"0{mins}"
        if secs<10:
            secs=f"0{secs}"
            
        timer=f"{mins}:{secs}"
        
        print(timer,end="\r")
        time.sleep(1)
        seconds-=1
    print("Time up!")

countdown(seconds)