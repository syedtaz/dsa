pub struct Solution;

impl Solution {
  pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    let mut res = Vec::with_capacity(nums.len() * 2);
    for _ in 0..2 {
      nums.iter().for_each(|x| res.push(*x));
    }
    res
  }
}