import my_oled
import time

state = 0

while True:
    print(state)
    #pass

    if state == 0:
        my_oled.print_text("test",0,0)
    
    if state == 1:
        my_oled.print_text("something else",0,0)

        
    time.sleep(1)

    state = state + 1
    
    if state >= 4:
        state = 0

    
