<<<<<<< HEAD
def combination(n,k):
    if k==n or k==0:
        return 1
    else :
        return combination(n-1,k-1) + combination(n-1,k)
print(combination(4,2))
=======
def com(n , k):
    if k==n or k==0:
        return 1
    else :
        return com(n-1 , k-1) + com(n-1,k)
print(com(4,2))        
>>>>>>> b44c4585a309162c64a377faf3d3e703ab98513a
