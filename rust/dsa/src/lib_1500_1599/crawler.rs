pub struct Solution {}

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut level: u32 = 0;

        for log in logs {
            match log.as_str() {
                "./" => {
                    continue;
                }
                "../" => {
                    level = level.saturating_sub(1);
                }
                _ => {
                    level += 1;
                }
            }
        }

        level as i32
    }
}
