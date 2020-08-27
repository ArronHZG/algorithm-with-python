'''
小马智行(Pony.ai)在广州南沙区有一支稳定运营的自动驾驶车队，可以将南沙区的地图看做一个二维的网格图，小马智行的广州office在(0, 0)位置。
公司现在有n台车，每天会按如下规则从围绕南沙区进行路测：
1. 初始n辆车都在公司。
2. 放眼整个南沙地图，每过一分钟， 若有一个网格的车数大于等于8， 则这个网格同时会有8辆车分别前往上，下，左，右，左上，左下，右上，右下的网格，不停执行该步骤直到所有的车辆的位置都固定不变。
作为小马智行车辆控制中心的一员， 你需要监管车辆运营的情况， 你需要等到所有车辆的位置固定之后，进行q次抽样统计， 每次需要统计出以(x_1, y_1)为左下角，以(x_2, y_2)为右上角的矩形范围内车辆的车辆的数目。
'''


def descri_car(n, intial_loc, dict):
    if n < 8:
        dict[tuple(intial_loc)] = n
        return
    else:
        every_num = n // 8
        sur = list()
        sur.append([intial_loc[0] + 0, intial_loc[1] + 1])
        sur.append([intial_loc[0] + 0, intial_loc[1] + -1])
        sur.append([intial_loc[0] + 1, intial_loc[1] + 0])
        sur.append([intial_loc[0] + -1, intial_loc[1] + 0])
        sur.append([intial_loc[0] + 1, intial_loc[1] + -1])
        sur.append([intial_loc[0] + -1, intial_loc[1] + 1])
        sur.append([intial_loc[0] + 1, intial_loc[1] + 1])
        sur.append([intial_loc[0] + -1, intial_loc[1] + -1])
        dict[tuple(intial_loc)] = n
        for i in range(8):
            if not dict.get(tuple(sur[i])):
                dict[tuple(sur[i])] = every_num
                dict[tuple(intial_loc)] = dict[tuple(intial_loc)] - every_num
            else:
                dict[tuple(sur[i])] += every_num
                dict[tuple(intial_loc)] = dict[tuple(intial_loc)] - every_num
        temp_dic = {}
        for i in dict.keys():
            if dict[i] >= 8:
                temp_dic[i] = dict[i]
                # print(temp)
        for i in temp_dic.keys():
            temp = dict[i]
            descri_car(temp, i, dict)


def car_number(loc, dict):
    x1, y1, x2, y2 = loc[0], loc[1], loc[2], loc[3]
    key = list(dict.keys())
    sum = 0
    for i in key:
        if i[0] >= x1 and i[0] <= x2 and i[1] >= y1 and i[1] <= y2:
            sum += dict[i]
    return sum


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    i = 0
    ins_sym = list()
    # 每个元素是一个列表，具有4个元素，分别是两组坐标
    while i < m:
        data = list(map(int, input().split()))
        ins_sym.append(data)
        i += 1
    # 两个函数，一个分配位置，一个计算数目
    intial_loc = [0, 0]
    dict = {}
    descri_car(n, intial_loc, dict)
    for i in ins_sym:
        print(car_number(i, dict))
