def bedroom():
    print('You are in a bedroom. A window is open and the sun is shining in.')
    print('There is a cell phone, resting on top of a chest of drawers.')
    print('north: Hallway')
    print('south: Bathroom')
    choice = input('? ')
    if choice == 'north':
        hallway()
    elif choice == 'south':
        bathroom()
    else:
        bedroom()

def bathroom():
    print('You are in a small bathroom. Everything is sparkling clean, except')
    print('there is toothpaste smeared on the counter. One small window lets')
    print('a bright beam of sunshine in.')
    print('north: Bedroom')
    choice = input('? ')
    if choice == 'north':
        bedroom()
    else:
        bathroom()

