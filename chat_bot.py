replies = {
    'hey': 'hey you',
    'how are you': 'doing great, thanks for asking',
    'whats up': 'nada mucho'



}

human_response = None
while human_response != "bye":
    human_response = input('?')
    if human_response in replies: 
        robot_response = replies[human_response]
        print(robot_response)
    else:
        print('Que?')
