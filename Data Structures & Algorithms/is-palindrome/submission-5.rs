impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        
        let bytes_str = s.as_bytes();
        let mut ep = s.len() -1;
        let mut sp = 0;

        while sp < ep {

            while sp < ep && !bytes_str[sp].is_ascii_alphanumeric() {
                sp += 1;
            }

            while ep > sp && !bytes_str[ep].is_ascii_alphanumeric(){
                
                ep -= 1;
            }

            
            if bytes_str[sp].to_ascii_lowercase() != bytes_str[ep].to_ascii_lowercase(){
                return false    
            }

            sp += 1;
            if ep == 0 {break;}
            ep -= 1;
        }
        true

    }
}
