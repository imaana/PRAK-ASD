def faktorPrima(x):
    factorlist=[]
    a=2
    while a<=x:
        if x%a==0:
            x/=a 
            factorlist.append(a)
        else:
            a+=1
    return factorlist

