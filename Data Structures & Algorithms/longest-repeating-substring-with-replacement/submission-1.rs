impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {

        use std::collections::HashMap;

        let mut map = HashMap::<_, i32>::new();
        let len = s.len();
        let by = s.as_bytes();
        let mut l = 0;
        let mut max_val = 0;
        for r in 0..len{
            let cc = by[r];
            *map.entry(cc).or_default() += 1;

            while  ((r - l + 1) - *map.values().max().unwrap() as usize) > k as usize{
                *map.get_mut(&by[l]).unwrap() -= 1;
                l +=1;
            }

            max_val = max_val.max(r - l + 1);

        }

        return max_val as _

    }
}
