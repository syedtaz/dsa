pub struct Solution {}

impl Solution {
    pub fn find_duplicates(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len() {
            let rf = nums[i].abs() as usize;
            nums[rf - 1] *= -1;
        }

        let mut res = Vec::with_capacity(nums.len());

        for i in 0..nums.len() {
            let rf = nums[i].abs() as usize;
            if nums[rf - 1] > 0 {
                res.push(nums[i].abs());
                nums[rf - 1] *= -1;
            }
        }

        res
    }
}
