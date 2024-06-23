#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i: i32 = 0;
        let mut j: i32 = nums.len() as i32 - 1 ;

        loop {
            if i > j {
                return i as i32;
            }

            if nums[i as usize] != val {
                i = i + 1;
                continue;
            }

            if nums[j as usize] != val {
                nums[i as usize] = nums[j as usize];
                i += 1;
            }

            j -= 1
        }
    }
}
