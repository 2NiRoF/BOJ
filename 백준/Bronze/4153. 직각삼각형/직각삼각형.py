while True:
    nums = [int(x) for x in input().split()]
    if not nums == [0,0,0]:
        nums.sort()
        if nums[-1]**2 == nums[0]**2 + nums[1]**2:
            print('right')
        else: print('wrong')
    else:
        break