impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {

        // let (mut start, mut end)  = (0, height.len() -1 );

        // let mut max_left = height[0];
        // let mut max_right = height[height.len() - 1];
        // let mut ans  = 0;
        // while start < end {

        //     let (left, right) = (height[start] , height[end]);
        //     if left < right {
        //         // let can_hold = 
        //         max_left = max_left.max(left);
        //         ans += (max_left - left);
        //         start += 1;
                
                
        //     } else {

        //         end -= 1;
        //         max_right = max_right.max(right);
        //         ans += (max_right - right);
        //     }
        // }

        let  max_left = {

            let mut left = Vec::with_capacity(height.len());
            let mut prev_max = 0;
            for i in 0..height.len() {
                left.push(prev_max);
                prev_max = prev_max.max(height[i]);
            }
            left
        };

        let max_right : Vec<_>  = {
            let mut left = Vec::with_capacity(height.len());
            let mut prev_max = 0;
            for i in (0..height.len()).rev() {
                left.push(prev_max);
                prev_max = prev_max.max(height[i]);
            }
            left.into_iter().rev().collect()
        };

        let mut ans = 0;

        for i in 0..height.len() {

            let h = height[i];
            let min_val = max_right[i].min(max_left[i]);
            if h <= min_val{
                ans += (min_val - h)
            }
        }

        ans

    }
}
