#Brute Force method
import sys
def findmaximumproduct(A):
    if len(A)<2:
        return
    max_product=-sys.maxsize
    max_i=max_j=-1
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]*A[j]>max_product:
                max_product=A[i]*A[j]
                max_i,max_j=i,j
    print(f"The maximum product is {max_product} and the pair is {(A[max_i],A[max_j])}")
if __name__=="__main__":
    A = [-10, -3, 5, 6, -2]
    findmaximumproduct(A)
