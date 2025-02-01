def findmaxlensublist(nums,target):
    d={}
    d[0]=-1
    total=0
    length=0
    ending_index=-1
    for i in range(len(nums)):
        total+=nums[i]
        if total not in d:
            d[total]=i
        if (total-target) in d and length<i-d[total-target]:
            length=i-d[total-target]
            ending_index=i
    print((ending_index-length+1,ending_index))
if __name__=="__main__":
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
    findmaxlensublist(nums,target)