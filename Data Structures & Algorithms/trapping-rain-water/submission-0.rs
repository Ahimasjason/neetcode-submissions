impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {

        let (mut start, mut end)  = (0, height.len() -1 );

        let mut max_left = height[0];
        let mut max_right = height[height.len() - 1];
        let mut ans  = 0;
        while start < end {

            let (left, right) = (height[start] , height[end]);
            if left < right {
                // let can_hold = 
                max_left = max_left.max(left);
                ans += (max_left - left);
                start += 1;
                
                
            } else {

                end -= 1;
                max_right = max_right.max(right);
                ans += (max_right - right);
            }
        }

        ans

    }
}
