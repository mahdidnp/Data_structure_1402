def power(q,p):
    if p==1:
        return q
    else:
        return q*power(q,p-1)
    
print (power(2,3))