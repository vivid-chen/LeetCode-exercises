def heapify(arr, n, i): 
    if i == -1:return
    largest = i # 这里都是指下标
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[largest] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
    

  
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 创建一个最大堆
    for i in range(n//2-1, -1, -1): 
        heapify(arr, n, i)

    # 一个个交换元素
    for i in range(n-1, -1, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        
        # 交换之后还原最大堆 
        for j in range(i//2-1, -1, -1):
            heapify(arr,i,j)
  
arr = [1,2,3,4,5,6,7,8,9] 
heapSort(arr) 
n = len(arr) 
print ("排序后") 
for i in range(n): 
    print ("%d" %arr[i])