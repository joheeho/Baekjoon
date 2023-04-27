n=int(input())
lst=[]
def check_string_int(lst):
    total=0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if '0' <= lst[i][j] <='9':
                total+=int(lst[i][j])
            else:
                pass
    return total

for i in range(n):
    lst.append(input())

lst.sort(key= lambda x:(len(x),check_string_int(x),x))
for x in lst:
    print(x)
