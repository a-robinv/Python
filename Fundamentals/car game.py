command = ""
started = False

while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('car already started')
        else:
            started = True
            print('Car started, ready to go')
    elif command == 'stop':
        if not started:
            print('car not started')
        else:
            started = False
            print('car stopped')
    elif command =='help':
        print("""
start - to start
stop - to stop
quit - to quit """)
    elif command == 'quit':
        break
    else:
        print("I don't understand")