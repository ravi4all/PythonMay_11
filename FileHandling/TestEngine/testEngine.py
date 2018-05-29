options = [
    ['1995','1990','1989','1991'],
    ['3.6','3.7','3.5','3.8'],
    ['skip','pass','continue','next'],
    ['1','5','Any number of values','2'],
    ['List','Tuples','Dictionary','Sets']
]

answers = ['1990','3.6','continue','Any number of values','Tuples']

file = open('questions.txt')

questions = file.readlines()

counter = 0

for i in range(len(questions)):
    print(questions[i])

    # print(options[i])
    for j in range(1):
        print("1. {}     2. {}".format(options[i][0],options[i][1]))
        print("3. {}     4. {}".format(options[i][2],options[i][3]))

    user_ans = int(input("Enter your answer : "))

    if options[i][user_ans-1] == answers[i]:
        counter += 1
        print("Correct Ans")
    else:
        print("Wrong Answer")

print("Final Score is",counter)


