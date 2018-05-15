import random

outcomes = [1,2,3,4,5,6,'out','no','wide']
score = 0

total_ball = 1

while total_ball < 7:
    outcome = random.choice(outcomes)

    if outcome == 'out':
        print("Ball {} => Out".format(total_ball))
        total_ball += 1
        continue
    elif outcome == 'wide':
        print("Ball {} => Wide".format(total_ball))
        score += 1
    elif outcome == "no":
        print("Ball {} => No".format(total_ball))
        score += 1
    elif outcome == 1:
        print("Ball {} => 1 run".format(total_ball))
        score += 1
        total_ball += 1
    elif outcome == 2:
        print("Ball {} => 2 run".format(total_ball))
        score += 2
        total_ball += 1
    elif outcome == 3:
        print("Ball {} => 3 run".format(total_ball))
        score += 3
        total_ball += 1
    elif outcome == 4:
        print("Ball {} => 4 run".format(total_ball))
        score += 4
        total_ball += 1
    elif outcome == 5:
        print("Ball {} => 5 run".format(total_ball))
        score += 5
        total_ball += 1
    elif outcome == 6:
        print("Ball {} => 6 run".format(total_ball))
        score += 6
        total_ball += 1

print("Total Score is",score)