#Using sorting
def findmaximumproduct(A):
    if len(A)<2:
        return
    A.sort()
    n=len(A)
    if (A[0]*A[1])>(A[n-1]*A[n-2]):
        print(f"Maximum product is {A[0]*A[1]} and the pair is {(A[0],A[1])}")
    else:
        print(f"Maximum product is {A[n-1]*A[n-2]} and the pair is {A[n-1]*A[n-2]}")
if __name__=="__main__":
    A = [-10, -3, 5, 6, -20]
    findmaximumproduct(A)