import random
score = 0  # tracks the scores
catalog = open("quizQuestions.csv", "r")  # opens the CSV file and stores it to question catalog
ques_set = catalog.readlines()  # reads the CSV file line by line
r = []  # list created to randomize 3 questions out
for i in range(3):
    r.append(random.randint(0, 8))
j = 0  # index to the list r
total = 0  # limiting the number of question to 3
questions = []  # list of questions
optA = []  # option A for all the questions
optB = []  # option B for all the questions
optC = []  # option C for all the questions
answers = []  # correct answers for al the questions
while total < 3:

    for q in ques_set:
        catalog_split = q.split(",")  # split in order to separate the questions, options and answers
        questions.append(catalog_split[0])
        optA.append(catalog_split[1])
        optB.append(catalog_split[2])
        optC.append(catalog_split[3])
        answers.append(catalog_split[4])

    for i in r:
        print(questions[r[j]])
        print(optA[r[j]])
        print(optB[r[j]])
        print(optC[r[j]])
        a = input("Enter the option :")

        answers[i] = answers[i].strip()
        if a == answers[i]:
            print("The answer is correct!!")
            score = score + 1
        else:
            print("Wrong...")

        j = j + 1
        total = total + 1
if score > 0:
    print("Congratulations! Your score is : ", score, "!!")
else:
    print("Sorry you have got them wrong...")








