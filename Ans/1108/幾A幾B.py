correct_ans_arr = [str(v) for v in input()]
guess_arr = [str(v) for v in input()]
a = int(0)
b = int(0)
repeat_num = [None]
correct_index = [None]
for i in range(len(correct_ans_arr)):
    if correct_ans_arr[i] == guess_arr[i]:
        a += 1
        correct_index.append(i)
for j in range(len(guess_arr)):
    for k in range(len(correct_ans_arr)):
        if correct_ans_arr[k] == guess_arr[j] and guess_arr[j] not in repeat_num and j not in correct_index and k not in correct_index:
            b += 1
            repeat_num.append(guess_arr[j])
print(f"{a}A{b}B")
1234567
7654321
