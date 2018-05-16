import random

outcomes = ['stone','paper','scissor']

my_score = 0
cpu_score = 0

while True:
    user_input = input("Enter your choice : ")
    cpu = random.choice(outcomes)

    if user_input == cpu:
        print("Match Tie")
    elif user_input == 'stone' and cpu == 'scissor':
        print("Your => {} CPU => {}".format(user_input,cpu))
        print("You win")
        my_score += 1
        print("Score : Player - {} CPU - {}".format(my_score,cpu_score))
    elif user_input == "paper" and cpu == 'stone':
        print("Your => {} CPU => {}".format(user_input, cpu))
        print("You win")
        my_score += 1
        print("Score : Player - {} CPU - {}".format(my_score, cpu_score))
    elif user_input == 'scissor' and cpu == 'paper':
        print("Your => {} CPU => {}".format(user_input, cpu))
        print("You win")
        my_score += 1
        print("Score : Player - {} CPU - {}".format(my_score, cpu_score))
    elif user_input == 'stone' and cpu == 'paper':
        print("Your => {} CPU => {}".format(user_input, cpu))
        print("CPU win")
        cpu_score += 1
        print("Score : Player - {} CPU - {}".format(my_score, cpu_score))
    elif user_input == "paper" and cpu == 'scissor':
        print("Your => {} CPU => {}".format(user_input, cpu))
        print("CPU win")
        cpu_score += 1
        print("Score : Player - {} CPU - {}".format(my_score, cpu_score))
    elif user_input == 'scissor' and cpu == 'stone':
        print("Your => {} CPU => {}".format(user_input, cpu))
        print("CPU win")
        cpu_score += 1
        print("Score : Player - {} CPU - {}".format(my_score, cpu_score))
    else:
        print("Wrong Input")
        break