pub struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .fold(HashMap::new(), |mut acc, x| {
                *acc.entry(x).or_insert(0) += 1;
                acc
            })
            .into_iter()
            .filter(|(_, v)| *v > nums.len() / 3)
            .map(|(k, _)| *k)
            .collect()
    }
}
