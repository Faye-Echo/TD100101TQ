#元组的创建 不能进行修改
tupleA=()#空元组
tupleA=('abcd',89,9.13,'peter',[11,22,33])
print(type(tupleA))
print(tupleA)
#元组的查询（主要基于切片）
#for item in tupleA:
    #print(item)
#print(tupleA[2])
#print(tupleA[2:4])
#print(tupleA[2:])
#print(tupleA[::-1])
#print(tupleA[::-2])#表示反转字符串，每隔两个取一次
#print(tupleA[::-3])#表示反转字符串，每搁三个取一个
#print(tupleA[-2:-1:])#倒着取下标，为-2到-1区间的

#tupleA[0]='PythonHello'#错误的，无法被修改
#print(tupleA)
print(type(tupleA[4]))
tupleA[4][0]=23346
print(tupleA)#可以对数据集中的列表数据项进行修改

#tupleB=(123,)#当元组中只有一个数据项的时候，必须要在第一个数据项后面加上逗号
#print(type(tupleB))
#tupleC=tuple(range(10))
#print(tupleC)
tupleC=(1,2,3,4,3,4,4,1)
print(tupleC.count(4))#可以统计元素出现的次数