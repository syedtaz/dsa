pub struct Solution;

impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut res = nums.clone();
        nums.iter()
            .enumerate()
            .for_each(|(i, v)| res[i] = nums[(*v) as usize]);
        res
    }
}
