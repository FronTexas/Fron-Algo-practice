def containsCloseNums(nums, k):
    num_to_latest_position = {}
    
    for pos,n in enumerate(nums): 
        if n in num_to_latest_position and abs(pos - num_to_latest_position[n]) <= k: return True
        num_to_latest_position[n] = pos
    return False