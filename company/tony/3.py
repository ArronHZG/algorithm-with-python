# N = list(map(int, input().split()))
from collections import defaultdict

str_list = ['a=a1',
            'c=d',
            'a1=ee',
            'f>d',
            'c>a1',
            'd!=a1',
            'ee>f']

trees = {}
key_id_num = 0


def merge(id1, id2, trees, arr):
    for i in range(len(arr)):
        if arr[i][id1] == '.':
            arr[i][id1] = arr[i][id2]
            arr[id1][i] = arr[id2][i]
        elif arr[i][id1] == arr[i][id2]:
            pass
        elif arr[i][id1] != arr[i][id2]:
            if arr[i][id1] == '!=' and arr[i][id2] in ['>', '<']:
                arr[i][id1] = arr[i][id2]
                arr[id1][i] = arr[id2][i]
            elif arr[i][id1] in ['>', '<'] and arr[i][id2] == '!=':
                pass
            else:
                return False

    for u in trees[id2]:
        trees[id1].add(u)
    trees.pop(id2)

    return True


def insert(elem, trees):
    global key_id_num
    for key, val in trees.items():
        if elem in val:
            return key
    key_id_num += 1
    trees[key_id_num] = {elem}
    return key_id_num


def fun(s):
    arr = [['.'] * len(s) for _ in range(len(s))]
    for s in str_list:
        if '>' in s:
            elem = s.split('>')
            set1_id = insert(elem[0], trees)
            set2_id = insert(elem[1], trees)

            re = arr[set1_id][set2_id]
            if re == '!=' or re == '>' or re == '.':
                arr[set1_id][set2_id] = '>'
                arr[set2_id][set1_id] = '>'
            else:
                return False

        elif '<' in s:
            elem = s.split('<')
            set1_id = insert(elem[0], trees)
            set2_id = insert(elem[1], trees)

            re = arr[set1_id][set2_id]
            if re == '!=' or re == '<' or re == '.':
                arr[set1_id][set2_id] = '<'
                arr[set2_id][set1_id] = '<'
            else:
                return False

        elif '!=' in s:
            elem = s.split('!=')
            set1_id = insert(elem[0], trees)
            set2_id = insert(elem[1], trees)
            re = arr[set1_id][set2_id]
            if re == '=':
                return False
            elif re == '<' or re == '>':
                pass
            elif re == '.':
                arr[set1_id][set2_id] = '<'
                arr[set2_id][set1_id] = '<'
        else:
            elem = s.split('=')
            set1_id = insert(elem[0], trees)
            set2_id = insert(elem[1], trees)
            re = arr[set1_id][set2_id]
            if re == '=' or re == '.':
                arr[set1_id][set2_id] = '='
                arr[set2_id][set1_id] = '='
                if merge(set1_id, set2_id, trees, arr):
                    pass
                else:
                    return False
            else:
                return False
        for r in arr:
            print(r)

        print(trees)
    return True


print(fun(str_list))
