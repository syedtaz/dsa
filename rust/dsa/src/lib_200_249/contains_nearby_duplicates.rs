#![allow(dead_code)]

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut seen: HashMap<i32, usize> = HashMap::with_capacity(nums.len());

        for (idx, num) in nums.iter().enumerate() {
            if seen.contains_key(num) && (idx - *seen.get(num).unwrap()) as i32 <= k {
                return true;
            }
            seen.insert(*num, idx);
        }

        false
    }
}
