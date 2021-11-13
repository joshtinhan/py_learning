import math
man_job_quantity = int(input())
man_jobcost_matrix = dict()
check_min_cost = math.inf
min_jobcost_man = int()
for i in range(man_job_quantity):
    jobcost_array = [int(v) for v in (input().split(","))]
    for j in range(len(jobcost_array)):
        man_jobcost_matrix[f"{i},{j}"] = jobcost_array[j]


def set_dict_by(job, dict):
    new_dict = {}
    for index in dict:
        if index.split(",")[1] == str(job):
            new_dict[index] = man_jobcost_matrix[index]
    return min(new_dict, key=new_dict.get)


final_ans = []
for i in range(man_job_quantity):
    final_ans.append(set_dict_by(i, man_jobcost_matrix)[0])
print(final_ans)
# print(
#     dict(sorted(set_dict_by(1, man_jobcost_matrix).items(), key=lambda x: x[1])))
# new_dict = set_dict_by(1, man_jobcost_matrix)
# min_one = min(new_dict, key=new_dict.get)
# print(min(new_dict, key=new_dict.get))


# print(sorted(set_dict_by(1, man_jobcost_matrix).items(), key=lambda x: x[1]))
