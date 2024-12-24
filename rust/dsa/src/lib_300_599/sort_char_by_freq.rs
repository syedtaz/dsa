pub struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut order: Vec<(char, i32)> = s
            .chars()
            .fold(HashMap::with_capacity(60), |mut acc, x| {
                *acc.entry(x).or_insert(0) += 1;
                acc
            })
            .into_iter()
            .collect();

        order.sort_by(|a, b| b.1.cmp(&a.1));
        order
            .into_iter()
            .map(|(x, i)| {
                let mut res = String::new();
                for _ in 0..i {
                    res.push(x)
                }
                res
            })
            .collect()
    }
}