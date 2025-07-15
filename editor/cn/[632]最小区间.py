# 你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。 
# 
#  我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释： 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length == k 
#  1 <= k <= 3500 
#  1 <= nums[i].length <= 50 
#  -10⁵ <= nums[i][j] <= 10⁵ 
#  nums[i] 按非递减顺序排列 
#  
# 
#  
# 
#  Related Topics 贪心 数组 哈希表 排序 滑动窗口 堆（优先队列） 👍 509 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        nums = sorted((num,i) for i,arr in enumerate(nums) for num in arr)
        cnt = defaultdict(int)
        left = 0
        ans = (float('-inf'),float('inf'))
        for num,i in nums:
            cnt[i] += 1
            while len(cnt) == k:
                ans = (nums[left][0],num) if ans[1]-ans[0] > num-nums[left][0] else ans
                cnt[nums[left][1]] -= 1
                if not cnt[nums[left][1]]:
                    del cnt[nums[left][1]]
                left += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
