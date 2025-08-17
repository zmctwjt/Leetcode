# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。 
# 
#  请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= barcodes.length <= 10000 
#  1 <= barcodes[i] <= 10000 
#  
# 
#  Related Topics 贪心 数组 哈希表 计数 排序 堆（优先队列） 👍 205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        heap = [[-v, k] for k, v in cnt.items()]
        heapify(heap)
        prev = [0, 0]
        for i in range(len(barcodes)):
            prev = heapreplace(heap, prev)
            prev[0] += 1
            barcodes[i] = prev[1]
        return barcodes
# leetcode submit region end(Prohibit modification and deletion)
