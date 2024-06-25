#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let s = nums.iter().fold(0, |acc, x| acc + x);
        let x = nums.len() * (nums.len() + 1) / 2;
        x as i32 - s
    }
}
