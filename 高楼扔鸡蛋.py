def superEggDrop(K:int,N:int)->int:
    # K 是鸡蛋个数
    # N是楼层总数

    memo = dict()
    def dp(K,N)->int:
        # base case
        if K == 1:return N
        if N == 0:return 0
        if (K,N) in memo:
            return memo[(K,N)]
        
        res = float('INF')
        for i in range(1,N+1): # 这里隐含的意思是第i层扔了之后变成两种可能的子状态
            res = min(res, # min用来取第一次扔遍历每一层的最少的操作数，取得至少的结果
                      max( # max代表第一次已经在第i层扔了之后两类子情况的最坏情况操作数
                          dp(K,N-i), # 鸡蛋没碎
                          dp(K-1,i-1) # 鸡蛋碎了
                      ) + 1 # 这里也是一次操作
            )
        memo[(K,N)] = res
        return res
    return dp(K,N)

print(superEggDrop(2,100))

print("ok")
