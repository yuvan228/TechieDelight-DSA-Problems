def sorting(A):
    zeros=A.count(0)
    k=0
    while zeros:
        A[k]=0
        zeros-=1
        k+=1
    for i in range(k,len(A)):
        A[i]=1
if __name__=="__main__":
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sorting(A)
    print(A)