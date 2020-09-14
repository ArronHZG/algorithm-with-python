def fun():
    def match(w, s):
        if len(w) != len(s):
            return False

        for i in range(len(w)):
            if w[i] in pair:
                if s[i] == pair[w[i]]:
                    continue
                else:
                    return False
            elif s[i] in pair:
                if w[i] == pair[s[i]]:
                    continue
                else:
                    return False
        return True

    def dfs(inx_seq, words):
        if inx_seq == len_seq:
            print('pair', pair)
            multi_pair.append(pair.copy())
            return
        seq = seq_word[inx_seq]
        # 判断 w 是否 可以配对
        t = True
        for c in seq:
            if c in pair:
                continue
            else:
                t = False
        if t:
            dfs(inx_seq + 1, words)

        for i in range(len(words)):
            w = words[i]
            if match(seq, w):
                arr = set()
                for j in range(len(seq)):
                    if seq[j] not in pair:
                        arr.add(seq[j])
                        arr.add(w[j])
                        pair[seq[j]] = w[j]
                        pair[w[j]] = seq[j]
                dfs(inx_seq + 1, words[:i] + words[i + 1:])
                for a in arr:
                    pair.pop(a)

    words = ['AA', 'BB', 'CC']

    seq = 'GG.'

    words = ['CAT', 'A', 'DOG', 'AND']

    seq = 'Z YZT ZVX Z XUW.'

    seq_word = seq[:-1].split(' ')

    # 按照字符串长度排序
    # words = sorted(words, key=lambda x: len(x))
    # seq_word = sorted(seq_word, key=lambda x: len(x))

    len_seq = len(seq_word)

    pair = {}
    multi_pair = []
    dfs(0, words)

    if len(multi_pair) == 1:
        pair = multi_pair[0]
        result = []
        for c in seq[:-1]:
            if c == ' ':
                result.append(' ')
            else:
                result.append(pair[c])
        result = ''.join(result)
        print(result)
    elif len(multi_pair) > 1:
        print('-')


fun()
