def asker(acceptable_options=None):

    user_input = None 
    while user_input not in acceptable_options:
        print(acceptable_options)
        user_input = input('?') 

options = [
    'yes',
    'no',
    'maybe',
]
asker(acceptable_options=options)
