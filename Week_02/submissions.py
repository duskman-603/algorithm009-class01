
class Solution:
    def isangram(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        list_s = list(s)
        list_t = list(t)
        # 排序的时间复杂度为nlogn
        list_s.sort(key=lambda x: ord(x))
        list_t.sort(key=lambda x: ord(x))
        if list_t == list_s:
            return True
        return False

    def isangram_01(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        count1 = self.count_char(s)
        count2 = self.count_char(t)
        if count1 == count2:
            return True
        else:
            return False

    def count_char(self, string):
        dict_01 = {substr: 0 for substr in string}
        for item in string:
            if item in dict_01:
                dict_01[item] += 1
        return dict_01

    def isanagram(self, s, t):
        if len(s) != len(t):
            return False
        set_01 = set(s)
        set_02 = set(t)
        if set_01 == set_02:
            for char in set_01:
                if s.count(char) != t.count(char):
                    return False
            return True
        else:
            return False
