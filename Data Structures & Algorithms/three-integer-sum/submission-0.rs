impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {


        nums.sort();

        let mut rv = ::std::collections::HashSet::new();
        'main_loop : for i in 0..nums.len() -2 {

            let (mut start, mut end) = (i + 1, nums.len() -1 );

            while start  < end {
                let sum = nums[i] + nums[ start ] + nums[end];
                if sum == 0 {
                    rv.insert(vec![nums[i] , nums[start], nums[end]]);
                    start += 1;
                    end -= 1;
                    continue;
                }
                if sum < 0 {
                    start += 1;
                } else {
                    end -= 1;
                }
            }
        }

        rv.into_iter().collect()
        
    }
}
