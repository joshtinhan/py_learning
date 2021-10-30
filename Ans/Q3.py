answer = list(''.join(input("The correct answer is:").split()))
toll = int(input("The toll of students"))
scoreDict = dict()
questions_answer_by_student = dict()
correctRate = [0]*len(answer)
for i in range(toll):
    student_name_ans = input("The student name and answer:").split()
    questions_answer_by_student[student_name_ans[0]
                                ] = ''.join(student_name_ans[1:])
    scoreDict[student_name_ans[0]] = 0
for j in questions_answer_by_student:
    for index, value in enumerate(list(questions_answer_by_student[j])):
        if answer[index] == value:
            scoreDict[j] += 100/len(answer)
            correctRate[index] += 1
print(questions_answer_by_student)
for index in scoreDict:
    print(f"{index} {int(scoreDict[index])}")
for val in correctRate:
    print(f"{round(float(val/toll*100))}% ", end='')
