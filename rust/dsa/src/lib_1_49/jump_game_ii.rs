#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut acc: i32 = 0;
        let mut limit: usize = 0;
        let mut bound: usize = 0;

        for i in 0..nums.len() - 1 {
            limit = limit.max(nums[i] as usize + i);

            if i == bound {
                acc += 1;
                bound = limit;
            }
        }

        acc
    }
}
