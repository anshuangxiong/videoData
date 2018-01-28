
S='abcdefghijk'
# 利用range函数
for i in range(0,len(S),2):
    print(S[i])

# 利用enumerate函数
for (index,char) in enumerate(S):
    print(index)
    print(char)

# 利用zip函数
ta=[1,2,3]
tb=[9,8,7]
tc=['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)