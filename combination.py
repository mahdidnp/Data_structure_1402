def combination(n,k):
    if k==n or k==0:
        return 1
    else :
        return combination(n-1,k-1) + combination(n-1,k)
print(combination(4,2))