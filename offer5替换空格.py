# 将字符串中的空格用%20替代
def ReplaceBlank(string:str)->str:
    Length = len(string)
    if Length < 1:
        return False
    NumberOfBlank = 0
    for i in range(0,Length):
        if string[i] == ' ':
            NumberOfBlank += 1
    if NumberOfBlank == 0:
        return string
    NuwLength = Length + NumberOfBlank*2
    string_list = [[] for i in range(0,NuwLength)] # 因为py字符串不可修改，所以用list存储
    while Length > 0 :
        if string[Length-1] == ' ':
            string_list[NuwLength-1] = '0'
            string_list[NuwLength-2] = '2'
            string_list[NuwLength-3] = '%'
            NuwLength -= 3
            Length -= 1
        else:
            string_list[NuwLength-1] = string[Length-1]
            Length -= 1
            NuwLength -= 1
    return "".join(string_list)

print(ReplaceBlank(" we are good ! "))

# 同类型,两个排序的数组进行尾插入变一个排序数组,默认升序
def CombinTwoArray(array1,array2):
    len1 = len(array1)
    len2 = len(array2)
    if len1 == 0:
        return array2
    if len2 == 0:
        return array1
    if len1 < len2:
        array1,array2 = array2,array1
        len1,len2 = len2,len1
    len3 = len1 + len2
    array1 = array1 + [ 0 for i in range(0,len2)]
    while len3 > 0:
        if len1 == 0:
            array1[0:len3] = array2[0:len2]
            break
        if len2 == 0:
            break
        if array1[len1-1] >= array2[len2-1]:
            array1[len3-1] = array1[len1-1]
            len1 -= 1
            len3 -= 1
        else:
            array1[len3-1] = array2[len2-1]
            len2 -= 1
            len3 -= 1
    return array1

print(CombinTwoArray([1,5,6],[1,2,8]))