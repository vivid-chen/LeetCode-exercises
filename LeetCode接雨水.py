def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """

        size = len(height)
        
        if size <3:
            return 0
        ans = 0
        left, right = 0, size-1
        left_max, right_max = int(height[0]),int(height[-1])
        while left <= right:
                left_max = max(left_max,int(height[left]))
                right_max = max(right_max,int(height[right]))

                if left_max < right_max:
                        ans += left_max - int(height[left])
                        left += 1
                else:
                        ans += right_max - int(height[right])
                        right -= 1

        return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))