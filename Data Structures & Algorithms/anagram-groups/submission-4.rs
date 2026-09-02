impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;

        let mut map = HashMap::<String, Vec<String>>::new();

        for st in strs {
            let st_clone = st.clone();
            let mut st_v = st.into_bytes();
            st_v.sort();

            let string_sorted = unsafe {
                String::from_utf8_unchecked(st_v)
            };
            match map.get_mut(&string_sorted){
                Some(item) => item.push(st_clone),
                None => {
                    let x = vec![st_clone];
                    map.insert(string_sorted, x);
                }
            }
        }
        map.into_values().collect()

    }
}
