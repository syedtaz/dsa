pub struct Solution {}

use std::collections::HashMap;

impl Solution {
  pub fn first_uniq_char(s: String) -> i32 {
    let mut hashtbl : HashMap<char, (usize, usize)> = HashMap::with_capacity(s.len());

    for (i, c) in s.chars().enumerate() {
      match hashtbl.get_mut(&c) {
        None => {hashtbl.insert(c, (i, 1));},
        Some(v) => {
          v.1 = v.1 + 1;
        },
      }
    }

    let filtered : Vec<usize> = hashtbl.into_values().filter(|(i, v)| *v == 1).map(|(i, _)| i).collect();

    match filtered.is_empty() {
      true => -1,
      false => filtered.iter().fold(usize::max_value(), |acc : usize, x| acc.min(*x)) as i32
    }
  }
}