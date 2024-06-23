#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::with_capacity(s.len() / 2);

        for ch in s.chars().into_iter() {
            match ch {
                '(' => stack.push(')'),
                '{' => stack.push('}'),
                '[' => stack.push(']'),
                _ => {
                    if Some(ch) != stack.pop() {
                        return false;
                    }
                }
            }
        }

        stack.is_empty()
    }
}
