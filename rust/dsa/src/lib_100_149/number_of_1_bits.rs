#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let bound = match n != 0 {
            true => (n as f32).log2() as i32 + 1,
            false => 1,
        };

        let mut acc = 0;

        for i in 0..bound {
          acc += if (n >> i) & 1 == 1 { 1 } else { 0 };
        }

        acc
      }
}
