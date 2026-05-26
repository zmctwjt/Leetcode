# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。 
# 
#  每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j ： 
# 
#  
#  i + 1 需满足：i + 1 < arr.length 
#  i - 1 需满足：i - 1 >= 0 
#  j 需满足：arr[i] == arr[j] 且 i != j 
#  
# 
#  请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。 
# 
#  注意：任何时候你都不能跳到数组外面。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= arr.length <= 5 * 10⁴ 
#  -10⁸ <= arr[i] <= 10⁸ 
#  
# 
#  Related Topics 广度优先搜索 数组 哈希表 👍 286 👎 0
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        cnt = defaultdict(set)
        for i,num in enumerate(arr):
            cnt[num].add(i)
        target = len(arr)-1
        vis = set([0])
        dq = deque([0])
        ans = 0
        while dq:
            for _ in range(len(dq)):
                i = dq.popleft()
                if i == target:
                    return ans
                for j in (i+1,i-1):
                    if j >= 0 and j < len(arr) and j not in vis:
                        dq.append(j)
                        vis.add(j)
                for j in cnt[arr[i]]:
                    if j not in vis:
                        dq.append(j)
                        vis.add(j)
                del cnt[arr[i]]
            ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
