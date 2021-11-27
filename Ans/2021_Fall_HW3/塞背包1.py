quantity_limit = [int(v) for v in input().split()]
arr = []
for i in range(quantity_limit[0]):
    arr.append([int(v) for v in input().split()])
arrs_to_iterate = list(range(quantity_limit[0]))


# def Perm_k(arrs, k):
#     # 若輸入 [1,2,3]，則先取出1這個元素，將剩餘的 [2,3]中取出另一個元素得到 [[1,2],[1,3]]
#     # 同理，取出2或者3時，得到的分別是 [[2,1],[2,3]]和 [[3,1],[3,2]]
#     if len(arrs) == 1:
#         return [arrs]
#     if k == 1:
#         return list(map(lambda s: [s], arrs))  # 當 k 為 1 時，每(單)個元素都可以被選取
#     result = []  # 最終的結果（即全排列的各種情況）
#     for i in range(len(arrs)):
#         rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i個元素後剩餘的元素
#         rest_lists = Perm_k(rest_arrs, k-1)     # 剩餘的元素選取 k-1元素
#         lists = []
#         for term in rest_lists:
#             lists.append(arrs[i:i+1]+term)  # 將取出的第 i個元素加到剩餘全排列的前面
#         result += lists
#     return result
sum_arr = []


def Comb(arrs, d, k, s, result):
    sum = 0
    check_limit = quantity_limit[1]

    if d == k:
        # print(result)
        if len(result) > 1:
            for j in result:
                check_limit -= arr[j][0]
                sum += arr[j][1]
            if check_limit >= 0:
                sum_arr.append(sum)
            check_limit = quantity_limit[1]
            sum = 0
        else:
            check_limit -= arr[result[0]][0]
            sum += arr[result[0]][1]
            if check_limit >= 0:
                sum_arr.append(sum)
            check_limit = quantity_limit[1]
            sum = 0
    for i in range(s, len(arrs)):
        result.append(arrs[i])
        Comb(arrs, d+1, k, i+1, result)
        result.pop()


for i in range(quantity_limit[0]):
    Comb(arrs_to_iterate, 0, i+1, 0, [])


print(max(sum_arr))
