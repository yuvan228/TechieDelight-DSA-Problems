#Finding largest sublist having an equal number of 0s and 1s
def findlargestsublist(nums):
    d={}
    total=0
    d[0]=-1
    length=0
    ending_index=-1
    for i in range(len(nums)):
        if nums[i]==0:
            total+=-1
        else:
            total+=1
        if total in d:
            if length<i-d.get(total):
                length=i-d.get(total)
                ending_index=i
        else:
            d[total]=i
    if ending_index!=-1:
        print((ending_index-length+1,ending_index))
    else:
        print("No sublist exists")
if __name__=="__main__":
    nums = [0, 0, 1, 0, 1, 0, 0]
    findlargestsublist(nums)