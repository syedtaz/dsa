#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen: HashMap<char, usize> = HashMap::with_capacity(s.len());
        let mut i = 0;
        let mut acc = 0;

        for (j, ch) in s.chars().enumerate() {
            match seen.get(&ch) {
                Some(v) if v >= &i => {
                    i = *v + 1;
                }
                None | Some(_) => (),
            }

            acc = acc.max(j - i + 1);
            seen.insert(ch, j);
        }

        acc as i32
    }
}
