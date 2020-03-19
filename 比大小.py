# 现在有"abcdefghijkl”12个字符，将其所有的排列中按字典序排列，给出任意一种排列，说出这个排列在所有的排列中是第几小的？
'''
输入
第一行有一个整数n（0＜n＜=10000）;

随后有n行，每行是一个排列；

样例输入
3
abcdefghijkl
hgebkflacdji
gfkedhjblcia

输出
输出一个整数m，占一行，m表示排列是第几位；
样例输出
1
302715242
260726926
'''

#!/usr/bin/env python
# coding=utf-8
import sys
list = []
list_new = [] 
for line in sys.stdin:
	list_new = line.split()
	list.append(list_new) 
# print(list[1:4])
num = int(''.join(list[0]))
arr = [1]*12
for i in range(1,12):
	arr[i] = arr[i-1]*i
# print(arr)
for string in list[1:num+1]:
	sum = 0
	for i in range(12):
		count = 0
		for j in range(i+1,12):
			if "".join(string)[i ]> "".join(string)[j]:
				count += 1
		sum += count*arr[11-i]
	sum += 1    
	print(sum)