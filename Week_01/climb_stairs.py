class Solution2:

    def climbstairs(self, n):
        frt = 1
        sec = 2
        res = 0
        for i in range(3, n+1):
            res = frt + sec
            frt, sec = sec, res
        return max(n, res)

    def climbstairs_01(self, n):
        res_list = [0, 1]
        if n <= 0:
            return 0
        if n in (0, 1):
            return res_list[n]
        if n > 2:
            for i in range(3, n+1):
                res = self.climbstairs(i-1) + self.climbstairs(i-2)
                res_list.append(res)
            return res_list[n]

