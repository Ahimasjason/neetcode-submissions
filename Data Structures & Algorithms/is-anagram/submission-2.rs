impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        let mut set = [0u8; 26];

        for i in s.chars() {
            let c = i.to_ascii_lowercase() as usize  - 'a' as usize;
            set[c] += 1;
        }

        for i in t.chars() {
            let c = i.to_ascii_lowercase() as usize  - 'a' as usize;
            set[c] -= 1;
        }

        !set.iter().any(|i| *i != 0)

    }
}
