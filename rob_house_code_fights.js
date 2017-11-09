function houseRobber(nums) {
    var max_rob = new Array(nums.length).fill(0);
    for (var i in max_rob){
        if (i == 0){
        	max_rob[i] = nums[i]
        }
        else if (i==1){
        	max_rob[i] = Math.max(max_rob[i-1],nums[i])
        }
        else{
            max_rob[i] = Math.max(max_rob[i-1],nums[i] + max_rob[i-2])  
        }
    }
    return max_rob[max_rob.length - 1]
}
