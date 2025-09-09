nums = [4,5,6,7,0,1,2,3,3,3]
target = 0

if len(nums) <= 2:
    exit()
a = 0
b = len(nums)-1
c = b//2
while nums[a] > nums[b]:
    if nums[c] > nums[a]:
        a = c
        c = (b+c)//2
    else:
        b = c
        c = (a+c)//2

#i = b
print(a,c,b)
if nums[0] > target:
    newNums = nums[b+1:]
else:
    newNums = nums[:b+1]