pub struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();
        let mut acc: Vec<i32> = Vec::with_capacity(2);

        for (i, num) in nums.iter().enumerate() {
            match map.get(&(target - *num)) {
                Some(j) => {
                    acc.push(i as i32);
                    acc.push(*j as i32);
                    break;
                }
                None => {
                    map.insert(*num, i);
                }
            }
        }

        acc
    }
}
