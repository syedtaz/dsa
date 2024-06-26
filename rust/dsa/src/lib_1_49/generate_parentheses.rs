#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

pub fn f(x: usize, memo: &mut HashMap<usize, Vec<String>>) -> Vec<String> {
    match memo.get(&x) {
        Some(v) => v.to_vec(),
        None => {
            let mut res: Vec<String> = Vec::with_capacity(2_usize.pow(x as u32));

            for (l, r) in (0..x).into_iter().zip((0..=x - 1).into_iter().rev()) {
                for cl in f(l, memo) {
                    for lr in f(r, memo) {
                        res.push(format!("({}){}", cl, lr));
                    }
                }
            }

            let _ = memo.insert(x, res);
            return memo.get(&x).unwrap().to_vec();
        }
    }
}

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut memo: HashMap<usize, Vec<String>> = HashMap::with_capacity(n as usize);
        memo.insert(0, vec!["".to_string()]);
        f(n as usize, &mut memo)
    }
}
