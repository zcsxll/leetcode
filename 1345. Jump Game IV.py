from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        m = {}
        for p, val in enumerate(arr):
            if 0 < p < len(arr)-1 and val == arr[p-1] == arr[p+1]: #连续的数字只记录两端的index
                continue
            if val not in m.keys():
                m[val] = [p]
            else:
                m[val].append(p)
        # print(m)
        q = [(0, 0)] #BFS，从0开始跳，此时step=0
        flag = set([0]) #已访问过的index，不会访问第二次
        step = 0
        while q: #BFS开始
            p, step = q.pop(0)
            # print(p)
            if p == len(arr)-1:
                break
            # if p > 0 and p-1 not in flag:
            #     flag.add(p-1)
            #     q.append((p-1, step+1))
            # if p < len(arr)-1 and p+1 not in flag:
            #     flag.add(p+1)
            #     q.append((p+1, step+1))
            for pp in [p-1, p+1] + m[arr[p]]: #当前BFS可选的index
                if pp not in flag: #还没有达到过的index
                    if 0 <= pp < len(arr): #index合法
                        flag.add(pp) #记录index
                        q.append((pp, step+1)) #jump
        return step

arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [7]
arr = [6, 1, 9]
arr = [11,22,7,7,7,7,7,7,7,22,13]
arr = [68,-94,-44,-18,-1,18,-87,29,-6,-87,-27,37,-57,7,18,68,-59,29,7,53,-27,-59,18,-1,18,-18,-59,-1,-18,-84,-20,7,7,-87,-18,-84,-20,-27]
print(Solution().minJumps(arr))