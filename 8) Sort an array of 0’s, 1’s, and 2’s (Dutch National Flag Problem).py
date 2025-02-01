def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
def threewaypartition(A):
    start=mid=0
    end=len(A)-1
    pivot=1
    while mid<=end:
        if A[mid]<pivot:
            swap(A,start,mid)
            start+=1
            mid+=1
        elif A[mid]>pivot:
            swap(A,mid,end)
            end-=1
        else:
            mid+=1
if __name__=="__main__":
     A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
     threewaypartition(A)
     print(A)