#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn can_permute_palindrome(s: String) -> bool {
        let counter = HashMap::with_capacity(s.len());
        s.chars()
            .into_iter()
            .fold(counter, |mut acc, e| {
                *acc.entry(e).or_insert(0) += 1;
                acc
            })
            .into_values()
            .fold(0, |acc, x| acc + x % 2)
            <= 1
    }
}
