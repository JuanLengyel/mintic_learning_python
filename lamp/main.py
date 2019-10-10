from lamp import Lamp

def run():
    lamp = Lamp(is_turned_on=False)

    while (True):
        command = str(raw_input('''
        Input one of the following commands:
            turn o[n]
            turn of[f]
            [e]xit
        '''))

        if command == 'n':
            lamp.turn_on()
        elif command == 'f':
            lamp.turn_off()
        elif command == 'e':
            return
        else:
            print('Can\'t understand your input')
    
if __name__ == "__main__":
    run()