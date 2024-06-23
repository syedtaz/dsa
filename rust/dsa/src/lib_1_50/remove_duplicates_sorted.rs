#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 1 {
            return nums.len() as i32;
        }

        let mut j: usize = 0;
        let mut i: usize = 0;

        while j <= nums.len() - 1 {
            let ch = nums[j];
            j += 1;

            while j < nums.len() && nums[j] == ch {
                j += 1
            }

            nums[i] = ch;
            i += 1;
        }

        i as i32
    }
}
