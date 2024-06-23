#![allow(dead_code)]

struct Solution;

impl Solution {
  pub fn length_of_last_word(s: String) -> i32 {
      let l = s.trim_end_matches(' ');

      match l.char_indices().rev().find(|(_, c)| *c == ' ') {
          Some((i, _)) => (l.len() - i - 1) as i32,
          None => l.len() as i32,
      }
  }
}