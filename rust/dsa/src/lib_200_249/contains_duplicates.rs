#![allow(dead_code)]

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen: HashSet<i32> = HashSet::with_capacity(nums.len());

        for num in nums {
            if seen.contains(&num) {
                return true;
            }
            seen.insert(num);
        }

        false
    }
}
