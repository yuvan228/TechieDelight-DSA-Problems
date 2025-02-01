#Using swapping
def sorting(A):
    pivot=1
    j=0
    for i in range(len(A)):
        if A[i]<pivot:
            swap(A,i,j)
            j+=1
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
if __name__=="__main__":
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sorting(A)
    print(A)


    