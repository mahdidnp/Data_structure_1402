def com(n , k):
    if k==n or k==0:
        return 1
    else :
        return com(n-1 , k-1) + com(n-1,k)
print(com(4,2))        