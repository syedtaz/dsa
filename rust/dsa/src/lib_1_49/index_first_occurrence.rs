struct Solution;

use std::hash::{DefaultHasher, Hash, Hasher};

impl Solution {
    #[inline(always)]
    fn generate_hash(s: &str) -> u64 {
        let mut h = DefaultHasher::new();
        s.hash(&mut h);
        h.finish()
    }

    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() < needle.len() {
            return -1
        }

        let target = Solution::generate_hash(&needle);
        for i in 0..(haystack.len() - needle.len() + 1) {
            if Solution::generate_hash(&haystack[i..i + needle.len()]) == target {
                return i as i32;
            }
        }

        -1
    }
}
