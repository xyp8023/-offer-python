# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def __init__(self, s):
        self.s = s
    def replaceSpace(self):
        # self.s = s
        s_output=''
        if ' ' not in self.s:
            return self.s
        else:
            for string in self.s:
                if string ==' ':
                    s_output += '%20'
                else:
                    s_output += string

            return s_output


# s = 'hello world'
# s = 'helloworld '
s = ' helloworld'
Solution_s = Solution(s)
Result = Solution_s.replaceSpace()
print(Result)
