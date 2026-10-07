impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {

        // if s.len() == 1 { return 1}
        use std::collections::HashMap;


        // key idea is if that char cout is gt 1 then it is duplicate so we have to move the left pointer post that char
        let mut seen = HashMap::new();

        let mut result = 0;

        let mut left = 0;
        let mut right  = 0;
        let string = s.as_bytes();

        while right < s.len() {
                let right_c = string[right];
                
                if let Some(&idx)  =seen.get(&right_c) {
                
                        while left <= idx  {
                            let lc = string[left];
                            seen.remove(&lc);
                            left += 1;
                        }
                }
                seen.insert(right_c, right);
                result = result.max(right - left + 1);
                right += 1;


        }
        result as i32

    }
}
