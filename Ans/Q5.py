import math
inputArr = [int(v) for v in input("Please enter params:").split()]
[efficiency_0, efficiency_max, efficiency_acc,
    efficiency_time_peak, efficiency_dec] = inputArr
rest_time = int()
real_efficiency_max = efficiency_0 + efficiency_acc*efficiency_time_peak
before_time_peak_area = (
    efficiency_0 + real_efficiency_max) * efficiency_time_peak/2
maxArea = 0

# 給上底跟時間計算下底


def calc_efficiency_1(v0, dec, time):
    if v0 - dec*time > 0:
        return v0 - dec*time
    else:
        return 0


# 如果進入疲倦狀態時間降低效率到最低還比初始效率還高，rt就是10
if real_efficiency_max <= efficiency_max and calc_efficiency_1(real_efficiency_max, efficiency_dec,
                                                               10 - efficiency_time_peak) > efficiency_0:
    rest_time = 10
    maxArea = (real_efficiency_max + calc_efficiency_1(real_efficiency_max, efficiency_dec,
                                                       10 - efficiency_time_peak)) * (10 - efficiency_time_peak)/2
# 計算最高點後的左梯形加右梯形面積


def calc_break_time_area(real_max, dec, time, time_peak, e_init):
    return ((real_max + calc_efficiency_1(real_max, efficiency_dec, time)) * time + (e_init +
                                                                                     calc_efficiency_1(e_init, dec, 9-time_peak-time)) * (9-time_peak-time))/2


if rest_time != 10:
    for v in range(11 - efficiency_time_peak):
        if efficiency_0 - efficiency_dec * (9 - efficiency_time_peak - v) >= 0:
            maxArea = max(calc_break_time_area(real_efficiency_max, efficiency_dec, v,
                                               efficiency_time_peak, efficiency_0), maxArea)
            if maxArea == calc_break_time_area(real_efficiency_max, efficiency_dec, v,
                                               efficiency_time_peak, efficiency_0):
                rest_time = v + efficiency_time_peak
    # else:
    #     maxArea = calc_break_time_area(real_efficiency_max,efficiency_dec,)


print(f"rt={rest_time} {maxArea + before_time_peak_area}")
