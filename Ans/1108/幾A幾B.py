correct_ans_arr = [str(v) for v in input()]
guess_arr = [str(v) for v in input()]
a = int(0)
b = int(0)
repeat_num = [None]
for i in range(len(correct_ans_arr)):
    for j in range(len(guess_arr)):
        if i == j:
            if correct_ans_arr[i] == guess_arr[i]:
                a += 1
        else:
            if correct_ans_arr[i] == guess_arr[j] and guess_arr[j] not in repeat_num:
                b += 1
                repeat_num.append(guess_arr[j])
print(f"{a}A{b}B")
