from queue import Queue


class Solution:
    def compileSeq(self, input):
        # write code here
        arr = [int(x) for x in input.split(',')]
        memo = dict()
        for i in range(len(arr)):
            if arr[i] not in memo:
                memo[arr[i]] = [i]
            else:
                memo[arr[i]].append(i)
        res = []
        val = memo[-1]
        val.sort()
        q = list()
        for i in val:
            q.append(i)
        while q:
            g = q.pop(0)
            if g in memo:
                val = memo[g]
                val.sort()
                for i in val:
                    q.append(i)
            res.append(g)

        return ','.join([str(x) for x in res])


res = Solution().compileSeq("1,2,-1,1")
print(res)
