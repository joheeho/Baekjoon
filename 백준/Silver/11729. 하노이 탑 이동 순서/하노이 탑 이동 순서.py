n= int(input())
def tower_of_hanoi(n,source,destin,temp):
    if n>1:
        tower_of_hanoi(n-1,source,temp,destin)
        print(source,destin)
        tower_of_hanoi(n-1,temp,destin,source)       
    else:
        print(source,destin)
print(2**n-1)
tower_of_hanoi(n,1,3,2)

