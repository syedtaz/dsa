#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let pal: String = s
            .chars()
            .filter(|x| x.is_alphanumeric())
            .map(|x| x.to_ascii_lowercase())
            .collect();

        for (a, b) in pal.chars().zip(pal.chars().rev()) {
            if a != b {
                return false;
            }
        }

        true
    }
}
