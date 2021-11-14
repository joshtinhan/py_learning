import math
man_job_quantity = int(input())
man_jobcost_matrix = dict()
min_jobcost_man = int()
final_ans = {}
final_cost = int(0)

for i in range(man_job_quantity):
    jobcost_array = [int(v) for v in (input().split(","))]
    final_ans[str(i)] = {}
    for j in range(len(jobcost_array)):
        man_jobcost_matrix[f"{i},{j}"] = jobcost_array[j]


def set_dict_by(man_index, dict, type):
    arr = []
    for index in dict:
        if index.split(",")[type] == str(man_index):
            arr.append(index)
    return arr


def get_right_man_index(dict):
    max_value = math.inf
    minval = min(dict.values())
    arr = list(filter(lambda x: dict[x] == minval, dict))
    if len(arr) > 1:
        arr_key_sum = []
        arr_man_index = {}
        for i in arr:
            max_value = min(int(i[0]) + int(i[2]), max_value)
            if max_value == int(i[0]) + int(i[2]):
                arr_key_sum.append(i)
        if len(arr_key_sum) > 1:
            for i in arr_key_sum:
                arr_man_index[i[2]] = int(i[0])
            return min(arr_man_index.values()), min(arr_man_index, key=arr_man_index.get)
        else:
            return arr_key_sum[0][0], arr_key_sum[0][2]
    else:
        return arr[0][0], arr[0][2]


def del_existed(dict):

    pop_arr = []
    final_ans[str(get_right_man_index(dict)[0])] = get_right_man_index(dict)[1]
    cost = dict[f"{get_right_man_index(dict)[0]},{get_right_man_index(dict)[1]}"]
    for k in range(2):
        temp_index = get_right_man_index(dict)[k]
        for i in set_dict_by(temp_index, dict, k):
            pop_arr.append(i)
    for i in pop_arr:
        dict.pop(i, {})
    return cost


for i in range(man_job_quantity):
    final_cost += del_existed(man_jobcost_matrix)
print(final_ans)
print(",".join(final_ans.values()))
print(final_cost)
