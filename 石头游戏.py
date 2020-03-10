class Pair(object):
    def __init__(self,fir,sec):
        self.fir = fir
        self.sec = sec

def StoneGame(piles:list):
    # 初始化
    size = len(piles)

    # dp_pre = [Pair(0,0) for i in range(size)]
    # dp = [dp_pre for i in range(size)]
    dp = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            dp[i][j] = Pair(0,0)
    
    # base case
    for i in range(size):
        dp[i][i].fir = piles[i]
        dp[i][i].sec = 0
    
    # 状态转移
    for l in range(2, size+1):
        for i in range(size-l+1):
            j = l + i - 1
            # 先手选左边
            left = piles[i] + dp[i+1][j].sec
            # 先手选右边
            right =  piles[j] + dp[i][j-1].sec
            # 状态转移方程
            if left > right:
                dp[i][j].fir = left
                dp[i][j].sec = dp[i+1][j].fir
            else:
                dp[i][j].fir = right
                dp[i][j].sec = dp[i][j-1].fir
    res = dp[0][size-1]
    return res.fir - res.sec
    


print(StoneGame([3, 9, 1, 2]))
win = StoneGame([3, 9, 1, 2])
if win > 0:
    print("Win!")
else:
    print("Not win.")


