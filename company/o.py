chn = ['', '', 'shi', 'bai', 'qian']

# 单个数字对应的中文汉字
chnNumChar = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")

# 每个小节里面的独立计数
chn = ("", "十", "百", "千")


def SectionToChinese(section):
    result = ""
    unitPos = 0
    zero = True

    while section > 0:
        print(section)
        v = section % 10
        if v == 0:
            if not zero:
                zero = True
                result = chnNumChar[int(v)] + result
        else:
            zero = False
            strIns = chnNumChar[int(v)]
            strIns += chn[unitPos]
            result = strIns + result

        # 权位增加
        unitPos = unitPos + 1
        # 小节值除以10
        section //= 10

    return result


def read_num(num):
    result = ''
    zero = False
    pos = 0
    while num > 0:
        tmp = num % 10
        if tmp == 0:
            if not zero:
                zero = True
                result = str(tmp) + result
        else:
            zero = False
            tmp = str(tmp)
            print(pos)
            tmp = tmp + chn[pos]
            result = str(tmp) + result

        pos += 1
        num /= 10
    return result


a = SectionToChinese(100)
print(a)
