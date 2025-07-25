# 给你一个整数 mountainHeight 表示山的高度。 
# 
#  同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。 
# 
#  工人们需要 同时 进行工作以 降低 山的高度。对于工人 i : 
# 
#  
#  山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 
# 秒。例如： 
#  
# 
#  
#  山的高度降低 1，需要 workerTimes[i] 秒。 
#  山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。 
#  
#  
# 
# 
#  返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。 
# 
#  
# 
#  示例 1： 
# 
#  
#  输入： mountainHeight = 4, workerTimes = [2,1,1] 
#  
# 
#  输出： 3 
# 
#  解释： 
# 
#  将山的高度降低到 0 的一种方式是： 
# 
#  
#  工人 0 将高度降低 1，花费 workerTimes[0] = 2 秒。 
#  工人 1 将高度降低 2，花费 workerTimes[1] + workerTimes[1] * 2 = 3 秒。 
#  工人 2 将高度降低 1，花费 workerTimes[2] = 1 秒。 
#  
# 
#  因为工人同时工作，所需的最少时间为 max(2, 3, 1) = 3 秒。 
# 
#  示例 2： 
# 
#  
#  输入： mountainHeight = 10, workerTimes = [3,2,2,4] 
#  
# 
#  输出： 12 
# 
#  解释： 
# 
#  
#  工人 0 将高度降低 2，花费 workerTimes[0] + workerTimes[0] * 2 = 9 秒。 
#  工人 1 将高度降低 3，花费 workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12
#  秒。 
#  工人 2 将高度降低 3，花费 workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12
#  秒。 
#  工人 3 将高度降低 2，花费 workerTimes[3] + workerTimes[3] * 2 = 12 秒。 
#  
# 
#  所需的最少时间为 max(9, 12, 12, 12) = 12 秒。 
# 
#  示例 3： 
# 
#  
#  输入： mountainHeight = 5, workerTimes = [1] 
#  
# 
#  输出： 15 
# 
#  解释： 
# 
#  这个示例中只有一个工人，所以答案是 workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + 
# workerTimes[0] * 4 + workerTimes[0] * 5 = 15 秒。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= mountainHeight <= 10⁵ 
#  1 <= workerTimes.length <= 10⁴ 
#  1 <= workerTimes[i] <= 10⁶ 
#  
# 
#  Related Topics 贪心 数组 数学 二分查找 堆（优先队列） 👍 29 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def check(self, cur_height: int, workerTimes: List[int],mid: int):
        for i in workerTimes:
            temp = mid - i
            ls = 2
            while temp >= 0:
                cur_height -= 1
                if cur_height <= 0:
                    return True
                temp -= i * ls
                ls += 1

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        min_ = min(workerTimes)
        left,right = 1,sum(min_*(i+1) for i in range(mountainHeight))
        while left < right:
            mid = (left + right) //2
            if self.check(mountainHeight, workerTimes,mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)
