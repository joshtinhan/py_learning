from functools import partial


correct_ans_arr = [str(v) for v in input()]
guess_arr = [str(v) for v in input()]
dict_correct_ans_arr = dict()
dict_guess_arr = dict()
a = int(0)
b = int()
correct_position = []
correct_number_index = int()
for i in range(len(correct_ans_arr)):
    dict_correct_ans_arr[i] = correct_ans_arr[i]
    dict_guess_arr[i] = guess_arr[i]
for i in dict_correct_ans_arr:
    if dict_correct_ans_arr[i] == dict_guess_arr[i]:
        a += 1
        correct_position.append(i)
for i in range(len(correct_position)):
    dict_correct_ans_arr.pop(correct_position[i])
    dict_guess_arr.pop(correct_position[i])
for i in dict_guess_arr:
    if dict_guess_arr[i] in dict_correct_ans_arr.values():
        for j in dict_correct_ans_arr:
            if dict_correct_ans_arr[j] == dict_guess_arr[i]:
                correct_number_index = j
        dict_correct_ans_arr.pop(correct_number_index)
b = len(dict_guess_arr) - len(dict_correct_ans_arr)
print(f"{a}A{b}B")
