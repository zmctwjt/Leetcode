# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。 
# 
#  假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。 
# 
#  
#  例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。 
#  
# 
#  另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中） 
# 
#  给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成
# 此基因变化，返回 -1 。 
# 
#  注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA",
# "AAACGGTA"]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC",
# "AACCCCCC"]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  start.length == 8 
#  end.length == 8 
#  0 <= bank.length <= 10 
#  bank[i].length == 8 
#  start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成 
#  
# 
#  Related Topics 广度优先搜索 哈希表 字符串 👍 351 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        if startGene in bank:
            bank.remove(startGene)
        q = deque([startGene])
        step = 0
        while q:
            for _ in range(len(q)):
                sgene = q.popleft()
                if sgene == endGene:
                    return step
                for gene in bank.copy():
                    diff = 0
                    for i in range(8):
                        if sgene[i] != gene[i]:
                            diff += 1
                    if diff <= 1:
                        q.append(gene)
                        bank.remove(gene)
            step += 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
