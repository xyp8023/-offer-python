# -*- coding:utf-8 -*-
class Solution:
    def __init__(self, target, array):
        self.target = target
        self.array = array
    # array 二维列表

    def Find(self):
        # self.target = target
        # self.array = array
        if self.array == [[]]:
            return False
        row = len(self.array)
        col = len(self.array[0])
        if self.target < self.array[0][0] or self.target > self.array[row - 1][col - 1]:
            return False
        else:
            for num_row in range(row):
                if self.target in self.array[num_row]:
                    return True

            return False


target = 7
# array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
# array = [[1,2,8,9],[4,7,10,13]]
array =[[]]
Output = Solution(target, array)
Result = Output.Find()
print(Result)
#

