def findmaxlensublist(nums,target):
    length=0
    ending_index=-1
    for i in range(len(nums)):
        total=0
        for j in range(i,len(nums)):
            total+=nums[j]
            if total==target:
                if length<j-i+1:
                    length=j-i+1
                    ending_index=j
    print((ending_index-length+1,ending_index))   
if __name__=="__main__":
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
    findmaxlensublist(nums,target)


    