#![allow(dead_code)]

struct Solution;

use std::collections::HashSet;

pub fn set(state: u64, idx: usize) -> u64 {
    state | (1 << idx)
}

pub fn generate_list(state: u64, candidates: &Vec<i32>) -> Vec<i32> {
    let mut num = state;
    let mut acc : Vec<i32> = Vec::new();

    while num != 0 {
      let index = num.leading_zeros();
      num ^= 1 << index;
      acc.push(candidates[index as usize])
    }

    acc
}

pub fn f(x: i32, state: u64, candidates: &Vec<i32>, acc: &mut HashSet<u64>) -> () {
    match x == 0 {
        true => {
            acc.insert(state);
        }
        false => {
            for (idx, cand) in candidates.iter().enumerate().filter(|(_, y)| x - **y >= 0) {
                f(x - *cand, set(state, idx), candidates, acc);
            }
        }
    }
}

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut acc: HashSet<u64> = HashSet::new();
        f(target, 0_64, &candidates, &mut acc);
        acc.into_iter()
            .map(|x| generate_list(x, &candidates))
            .collect()
    }
}
