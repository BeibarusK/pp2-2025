def spy_game(nums):
    for i in range(len(nums)):
        if nums[0]==0 and nums[1]==0 and nums[2]==7:
            return True
        elif nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False
print(spy_game([1,2,4,0,2,7,5]))
print(spy_game([1,2,4,0,0,7,5]))