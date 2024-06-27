#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

pub fn f(i: usize, j: usize, m: usize, n: usize, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
    match memo.get(&(i, j)) {
        Some(v) => *v,
        None => {
            let res = {
                match (i == m, j == n) {
                    (true, true) => 1,
                    (true, false) => f(i, j + 1, m, n, memo),
                    (false, true) => f(i + 1, j, m, n, memo),
                    (false, false) => f(i, j + 1, m, n, memo) + f(i + 1, j, m, n, memo),
                }
            };
            memo.insert((i, j), res);
            res
        }
    }
}

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut memo: HashMap<(usize, usize), i32> = HashMap::new();
        f(1, 1, m as usize, n as usize, &mut memo)
    }
}
