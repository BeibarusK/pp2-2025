def has_33(nums):
    for i in range(len(nums)):
        if nums[0]==3 and nums[1]==3:
            return True
        elif nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([1,3,4]))