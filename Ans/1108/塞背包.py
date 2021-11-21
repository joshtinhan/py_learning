arr = []
quantity_limit = [int(v) for v in input().split()]
for i in range(quantity_limit[0]):
    arr.append([int(v) for v in input().split()])


def get_sum_list(list, index):
    sum = 0
    for i in range(len(list)):
        sum += list[i][index]
    return sum


def recu(comb, curr_index, limit, input_arr):
    while curr_index < len(input_arr):
        curr_weight = 0
        if len(comb) > 1:
            curr_weight = get_sum_list(comb, 1)
            if input_arr[curr_index][0] + curr_weight <= limit:
                comb.append(input_arr[curr_index])
            else:
                max_value = 0
                origin_value = get_sum_list(comb, 0)
                for i in range(len(comb)):
                    b = comb.pop(i)
                    max_value = max(origin_value, get_sum_list(
                        comb, 1)+arr[curr_index][1])
                    if get_sum_list(
                            comb, 1)+arr[curr_index][1] == max_value and get_sum_list(comb, 0)+arr[curr_index][0] <= limit:
                        comb.append(arr[curr_index])
                    else:
                        comb.insert(i, b)
                curr_index += 1
                recu(comb, curr_index, limit, input_arr)
        else:
            if input_arr[curr_index][0] <= limit:
                curr_weight = input_arr[curr_index][0]
                comb.append(input_arr[curr_index])

        curr_index += 1
        recu(comb, curr_index, limit, input_arr)
    return comb


print(get_sum_list(recu([], 0, quantity_limit[1], arr), 1))
