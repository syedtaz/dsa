#![allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut acc = HashMap::new();

        for str in strs.into_iter() {
            let mut key: Vec<char> = str.chars().collect();
            key.sort_unstable();
            acc.entry(key).or_insert(Vec::new()).push(str);
        }

        acc.into_values().collect()
    }
}
