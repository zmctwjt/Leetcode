# 给定一个整数数组
#  arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且
#  arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。 
# 
#  由于结果会非常大，请返回 10⁹ + 7 的模。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举(arr[i], arr[j], arr[k])：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= arr.length <= 3000 
#  0 <= arr[i] <= 100 
#  0 <= target <= 300 
#  
# 
#  Related Topics 数组 哈希表 双指针 计数 排序 👍 155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ans = 0
        for i in range(len(arr)-2):
            left=i+1
            right = len(arr)-1
            while left < right:
                temp = arr[i]+arr[left]+arr[right]
                if temp<target:
                    left += 1
                elif temp > target:
                    right -= 1
                else:
                    if arr[left] == arr[right]:
                        ans += (right-left+1)*(right-left)//2
                        break
                    temp_l = left
                    temp_r = right
                    left += 1
                    right -= 1
                    while left < temp_r and arr[left] == arr[left-1]:
                        left += 1
                    while temp_l < right and arr[right] == arr[right+1]:
                        right -=1
                    ans += (temp_r-right)*(left-temp_l)
        return ans % (10**9+7)

# leetcode submit region end(Prohibit modification and deletion)
