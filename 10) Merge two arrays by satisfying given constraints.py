def rearrange(X,Y):
    if not len(X):
        return
    k=0
    for i in range(len(X)):
        if X[i]:
            X[k]=X[i]
            k+=1
    for i in range(k,len(X)):
        X[i]=0
    merge(X,Y,k-1,len(Y)-1)
def merge(X,Y,m,n):
    k=m+n+1
    while m>=0 and n>=0:
        if X[m]>Y[n]:
            X[k]=X[m]
            k-=1
            m-=1
        else:
            X[k]=Y[n]
            k-=1
            n-=1
    while n>=0:
        X[k]=Y[n]
        k-=1
        n-=1
    for i in range(len(Y)):
        Y[i]=0
if __name__=="__main__":
    X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    Y = [1, 8, 9, 10, 15]
    rearrange(X,Y)
    print(X)
