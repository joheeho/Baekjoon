import sys
n=int(input())
company={}
for i in range(n):
    name, in_out = sys.stdin.readline().rstrip().split()
    if in_out=="enter":
        company[name]="enter"
    else:
        del company[name]
company=sorted(company.keys(),reverse=True)
for x in company:
    print(x)

