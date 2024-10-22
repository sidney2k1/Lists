x=[4,5,1,2,8,9,10,7]
print("Original list:",x)
count=0
for i in x:
    count+=i
avg=count/len(x)
print("sum=",count)
print("average=",avg)
x.sort()
print("smallest element is:",x[0])
print("largest element is:",x[-1])
