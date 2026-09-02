impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        let mut map = std::collections::HashMap::<i32, usize>::new();

        for (idx, val) in nums.into_iter().enumerate() {
            let diff = target - val ;
            match map.get(&diff) {
                Some(item)  => {

                    return vec![*item as i32 , idx as i32]
                },
                None => {
                    map.insert(val, idx);
                }
            }
        }
        vec![]

    }
}
