import random
user_input=str(input("choise from rock paper scissor "))
possible_action=['rock','paper','scissor']
computer_action=random.choice(possible_action)
if user_input==computer_action:
    print('you both chose',user_input)
    print('tie')
elif user_input=='rock':
    if computer_action=='sicssor':
        print('rock smashes scissor')
    else:
        print('rock is covered by paper')
        print('you lost')
elif user_input=='paper':
    if computer_action=='rock':
        print('rock is covered by paper')
        print('you won')
    else:
        print('paper is cut by scissor')
        print('you lost')
elif user_input=='scissor':
    if computer_action=='paper':
        print('paper is cut by scissor ')
        print('you won')
    else:
        print('rock smashes scissor')
        print('you lost')

