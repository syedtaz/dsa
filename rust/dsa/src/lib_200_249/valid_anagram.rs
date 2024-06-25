#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

pub fn generate_counter(s: &str) -> HashMap<char, usize> {
    let counter: HashMap<char, usize> = HashMap::with_capacity(s.len());

    s.chars().into_iter().fold(counter, |mut acc, e| {
        *acc.entry(e).or_insert(0) += 1;
        acc
    })
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        generate_counter(&s).eq(&generate_counter(&t))
    }
}
