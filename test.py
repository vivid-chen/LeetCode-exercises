def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(i[1],res[-1][1])
        return res

print(merge([[1,3],[2,6],[15,18],[8,10]]))