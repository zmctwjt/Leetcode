# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。 
# 
#  请你找到并返回这个整数 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  0 <= arr[i] <= 10^5 
#  
# 
#  Related Topics 数组 👍 125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        m = len(arr) // 4
        for i in (m,2*m+1):
            l = bisect.bisect_left(arr, arr[i])
            if arr[l+m] == arr[i] :
                return arr[i]
        return arr[3*m+2]

# leetcode submit region end(Prohibit modification and deletion)
