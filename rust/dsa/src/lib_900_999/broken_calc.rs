pub struct Solution;

impl Solution {
    pub fn broken_calc(start_value: i32, mut target: i32) -> i32 {
        let mut acc = 0;

        while target > start_value {
            acc += 1;
            match target & 1 == 0 {
                true => {
                    target /= 2;
                }
                false => {
                    target += 1;
                }
            }
        }

        acc + start_value - target
    }
}
