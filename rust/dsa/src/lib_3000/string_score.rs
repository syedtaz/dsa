pub struct Solution {}

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let conv: Vec<u32> = s.chars().map(|x| x as u32 - 48).collect();
        conv.iter()
            .zip(conv.iter().skip(1))
            .fold(0, |acc, (a, b)| acc + (*a).abs_diff(*b)) as i32
    }
}
