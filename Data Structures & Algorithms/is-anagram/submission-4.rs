impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        if s.len() != t.len() {
            return false;
        }
        
        let mut seen = [0; 26];
        let small_a = 'a' as usize;
        
        for idx in 0..s.len() {
            let stuff_s = s.chars().nth(idx).unwrap() as usize;
            let stuff_t = t.chars().nth(idx).unwrap() as usize;
            seen[stuff_s - small_a] += 1;
            seen[stuff_t - small_a] -= 1;
        }
        
        !seen.iter().any(|i| *i != 0)

    }
}
