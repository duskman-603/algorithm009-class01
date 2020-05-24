class Solution:

    def valid_palindrome(self, string):

        if not string:
            return True
        else:
            string = self.filter(string)
            res = ""
            n = len(string)
            for i in range(n):
                sub_char = string[n-i-1]
                res += sub_char
            if string == res:
                return True
            else:
                return False

    def valid_palindrome_01(self, string):
        n = len(string)
        if not string:
            if n == 0:
                return False
            return True
        else:
            string = self.filter(string)
            char_list = list(string)
            char_list_cp = char_list[:]
            char_list_cp.reverse()
            if char_list_cp == char_list:
                return True
            else:
                return False

    def valid_palindrome_02(self, string):

        if not string:
            return True
        else:
            string = self.filter(string)
            n = len(string)
            left = 0
            right = n-1
            while left < right:
                if string[left] == string[right]:
                    left += 1
                    right -= 1
                    continue
                return False
            return True

    def valid_palindrome_03(self, string):
        if not string:
            return True
        else:
            string = self.filter(string).lower()
            n = len(string)
            left = 0
            right = n-1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

    def filter(self, item):
        list_ = re.findall(_TARGET_STRING, item)
        return "".join(list_).lower()
