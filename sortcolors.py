# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.
def sortColors(nums):
    red = []
    white = []
    blue = []
    
    for i in range(len(nums)):
        if nums[i] == 0:
            red.append(nums[i])

        elif nums[i] == 1:
            blue.append(nums[i])

        else:
            white.append(nums[i])
    nums.clear()
    nums.extend(red)
    nums.extend(blue)
    nums.extend(white)
    
    return nums    

print(sortColors([2,0,2,1,1,0]))
  
