#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        match n {
            1 | 2 => n,
            _ => {
                let mut a = 1;
                let mut b = 2;

                for _ in 2..n {
                    let c = a + b;
                    a = b;
                    b = c;
                }

                b
            }
        }
    }
}
