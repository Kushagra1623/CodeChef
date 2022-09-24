t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    c=0
    if (x==0 or x==n):
        print(c)
    elif x <= (n-x):
        print(x)
    else:
        print(n-x)
        