pub struct Solution;

use std::cmp::Ordering;

impl Solution {
    fn split(
        nums: &Vec<i32>,
        key: fn(&i32, &i32) -> Ordering,
        filter: fn(&(usize, &i32)) -> bool,
    ) -> Vec<i32> {
        let mut buffer: Vec<i32> = nums
            .iter()
            .enumerate()
            .filter(filter)
            .map(|(_, x)| *x)
            .collect();

        buffer.sort_unstable_by(key);
        buffer
    }

    pub fn sort_even_odd(nums: Vec<i32>) -> Vec<i32> {
        let odds = Solution::split(&nums, |a, b| b.cmp(&a), |(i, _)| *i & 1 == 1);
        let evens = Solution::split(&nums, |a, b| a.cmp(&b), |(i, _)| *i & 1 == 0);
        let mut acc = vec![0; nums.len()];

        for (i, v) in odds.iter().enumerate() {
            acc[(2 * i) + 1] = *v;
        }

        for (i, v) in evens.iter().enumerate() {
            acc[2 * i] = *v;
        }

        acc
    }
}
