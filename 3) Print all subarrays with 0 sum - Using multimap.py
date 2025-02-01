def insert(d,key,value):
    d.setdefault(key,[]).append(value)
def printallsublists(nums):
    d={}
    insert(d,0,-1)
    total=0
    for i in range(len(nums)):
        total+=nums[i]
        if total in d:
            list=d.get(total)
            for value in list:
                print("Sublist is",(value+1,i))
        insert(d,total,i)
if __name__=="__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printallsublists(nums)
