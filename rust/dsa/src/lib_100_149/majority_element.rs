pub struct Solution {}

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        // Bayer-Moore
        let mut candidate = nums[0];
        let mut count = 1;

        for num in nums.into_iter().skip(1) {
            if num == candidate {
                count += 1;
                continue;
            }

            count -= 1;
            if count == 0 {
                candidate = num;
                count = 1;
            }
        }

        candidate
    }
}
