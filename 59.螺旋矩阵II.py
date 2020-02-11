def generateMatrix(n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 初始化上下左右边界
        t, b, l, r = 0, n-1, 0, n-1
        # 初始化矩阵
        mat = [[0 for i in range(n)]for i in range(n)]
        num,tar = 1, n**2
        while num <= tar:
            for i in range(l,r+1): # 从左到右
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t,b+1): # 从上到下
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r,l-1,-1): # 从右到左
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b,t-1,-1): # 从下到上
                mat[i][l] = num
                num += 1
            l += 1

        return mat

print(generateMatrix(3))