class Solution:
    def findanagrams(self, s, p):
        n1 = len(s)
        n2 = len(p)
        if n1 == 0 or n1 < n2:
            return []
        res = []
        for i in range(n1-n2+1):
            sub_str = s[i:n2+i]
            if self.isanagrams(sub_str, p):
                res.append(i)
        return res

    def count_ord(self, s):
        count = 0
        for item in s:
            count += ord(item)
        return count

    def isanagrams(self, s, t):
        count_s = self.count_(s)
        count_t = self.count_(t)
        if count_s == count_t:
            return True

    def count_(self, s):
        dict_01 = {item: 0 for item in s}
        for char in s:
            if char in dict_01:
                dict_01[char] += 1
        return dict_01

    def findanagrams_01(self, s, p):
        n1 = len(s)
        n2 = len(p)
        if not n1 or n1 < n2:
            return []
        p_list = [0]*26
        s_list = [0]*26
        res = []
        for p1 in p:
            p_list[ord(p1)-97] += 1
        left = 0
        for right in range(n1):
            if right < len(p)-1:
                s_list[ord(s[right])-97] += 1
                continue
            s_list[ord(s[right])-97] += 1
            if p_list == s_list:
                res.append(left)
            s_list[ord(s[left])-97] -= 1
            left += 1
        return res

