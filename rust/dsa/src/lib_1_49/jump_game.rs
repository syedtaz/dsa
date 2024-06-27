#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        (0..nums.len())
            .into_iter()
            .rev()
            .fold(nums.len() - 1, |acc, i| {
                if i + nums[i] as usize >= acc {
                    i
                } else {
                    acc
                }
            })
            == 0
    }
}
