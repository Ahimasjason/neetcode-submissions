impl Solution {
    pub fn has_duplicate(mut nums: Vec<i32>) -> bool {
        nums.sort();

        if nums.len() == 1 {return false}
        for i in 1..nums.len() {
            if nums[i] == nums[i - 1]{
                return true
            }
        }
        return false

    }
}
