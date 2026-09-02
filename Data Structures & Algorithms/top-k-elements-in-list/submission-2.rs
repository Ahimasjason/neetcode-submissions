impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map = std::collections::HashMap::<i32, usize>::new();

        for n in nums {

            *map.entry(n).or_insert(0) += 1
        }

        let mut v = map
        .into_iter()
        .map(|(key, freq)| {
            (freq , key)
        })
        .collect::<Vec<_>>();
        v.sort();
        
        v.into_iter().rev().take(k as usize).map(|(k, v)| v).collect()
    }
}
