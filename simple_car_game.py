is_the_car_running=False
commands=["start","stop","quit","help"]
while True:
    cmd=input('cmd:').lower()
    if cmd not in commands:
        print('''Sorry, I don't understant that please enter "help" to see the standard commands''')
    else:
        if cmd=="start" and is_the_car_running==False:
            is_the_car_running=True
            print("car starts")
        elif cmd=="start" and is_the_car_running==True:
            print('the car has already started')
        if cmd=="stop" and is_the_car_running==True:
            is_the_car_running=False
            print('car stops')
        elif cmd=="stop" and is_the_car_running==False:
            print('the car has already stoped')
        if cmd=="help":
            print('''"start"=start the car
"stop"=stop the car
"quit"=end of the game''')
        if cmd=="quit":
            print('end of the game')
            break