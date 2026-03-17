# 矩阵对角线 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。例如，矩阵 mat 有 6 行 3 列，从 mat[2
# ][0] 开始的 矩阵对角线 将会经过 mat[2][0]、mat[3][1] 和 mat[4][2] 。 
# 
#  给你一个 m * n 的整数矩阵 mat ，请你将同一条 矩阵对角线 上的元素按升序排序后，返回排好序的矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# 输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,2
# 5,68,4],[84,28,14,11,5,50]]
# 输出：[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66]
# ,[84,28,75,33,55,68]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 100 
#  1 <= mat[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 排序 👍 147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        distinct_list = []
        for i in range(m-1,-1,-1):
            z = 0
            j = i
            distinct = []
            while j < m and z < n:
                distinct.append((j,z))
                z += 1
                j += 1
            distinct_list.append(distinct)
        for i in range(1,n):
            z = 0
            j = i
            distinct=[]
            while z < m and j <n:
                distinct.append((z,j))
                z += 1
                j +=1
            distinct_list.append(distinct)
        ans = [[0]*n for _ in range(m)]
        for distinct in distinct_list:
            for i,(x,y) in enumerate(sorted(distinct,key=lambda x:mat[x[0]][x[1]])):
                xx,yy = distinct[i]
                ans[xx][yy] = mat[x][y]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
