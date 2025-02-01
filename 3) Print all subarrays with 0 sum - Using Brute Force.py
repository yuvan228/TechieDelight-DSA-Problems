def printallsublists(nums):
    for i in range(len(nums)):
        total=0
        for j in range(i,len(nums)):
            total+=nums[j]
            if total==0:
                print("Sublist:",(i,j))
if __name__=="__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printallsublists(nums)