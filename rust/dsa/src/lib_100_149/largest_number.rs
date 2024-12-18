pub struct Solution {}

impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut ss: Vec<String> = nums.into_iter().map(|x| x.to_string()).collect();
        let mlength = ss.iter().fold(0, |acc, x| acc.max(x.len()));
        let mut left_buffer = String::with_capacity(mlength);
        let mut right_buffer = String::with_capacity(mlength);

        ss.sort_by(|a, b| {
            left_buffer.clear();
            right_buffer.clear();
            left_buffer.push_str(a);
            left_buffer.push_str(b);
            right_buffer.push_str(b);
            right_buffer.push_str(a);

            left_buffer.cmp(&right_buffer)
        });

        match ss.first().unwrap().chars().nth(0).unwrap() {
            '0' => "0".to_owned(),
            _ => ss.into_iter().collect(),
        }
    }
}
