s=input()
s_list=[]
for i in range(len(s)):
    s_list.append(s[-i:])
s_list.sort()
for x in s_list:
    print(x)
