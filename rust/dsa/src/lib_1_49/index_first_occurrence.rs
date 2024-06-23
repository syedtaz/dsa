#![allow(dead_code)]

use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

struct Solution;

fn hash(slice: &str) -> u64 {
    let mut hasher = DefaultHasher::new();
    slice.hash(&mut hasher);
    hasher.finish()
}

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.len() > haystack.len() {
            return -1;
        }

        let target = hash(&needle);

        for i in 0..haystack.len() - needle.len() + 1 {
            if hash(&haystack[i..i + needle.len()]) == target {
                return i as i32;
            }
        }

        -11
    }
}
