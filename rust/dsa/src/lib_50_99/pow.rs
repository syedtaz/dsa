pub struct Solution;
pub struct Solution2;

// Recursive

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        match n == 0 {
            true => 1.0,
            false => {
                let res = Solution::my_pow(x, (n / 2).abs());
                match (n & 1 == 0, n < 0) {
                    (true, false) => res * res,
                    (true, true) => 1.0 / (res * res),
                    (false, false) => x * res * res,
                    (false, true) => 1.0 / (x * res * res),
                }
            }
        }
    }
}

// Iterative

impl Solution2 {
    fn helper(x: f64, n: i64) -> f64 {
        if x == 1.00 {
            return 1.0;
        }

        let mut acc = 1.0;
        let mut multiplier = x;
        let mut curr = n;

        if n < 0 {
            curr = n.abs();
            multiplier = 1.0 / x;
        }



        while curr != 0 {
            if curr & 1 == 1 {
                acc *= multiplier;
                curr -= 1;
            }
            multiplier = multiplier * multiplier;
            curr = curr >> 1;
        }

        acc
    }

    pub fn my_pow(x: f64, n: i32) -> f64 {
        Self::helper(x, n as i64)
    }
}
