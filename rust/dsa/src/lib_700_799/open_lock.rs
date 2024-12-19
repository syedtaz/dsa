pub struct Solution {}

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        let mut seen: HashSet<u16> = deadends
            .into_iter()
            .map(|x| x.parse::<u16>().unwrap())
            .collect();

        let target = target.parse::<u16>().unwrap();
        let mut queue = VecDeque::new();
        queue.push_back((0000, 0));

        while let Some((lock, moves)) = queue.pop_front() {
          if lock == target {
            return moves;
          }

          if seen.contains(&lock) {
            continue;
          }

          seen.insert(lock);

          for i in &[1000, 0100, 0010, 0001] {
            let wheel = (lock / i) % 10;
            queue.push_back(((lock - i * wheel) + (i * ((wheel + 1) % 10)), moves + 1));
            queue.push_back(((lock - i * wheel) + (i * ((wheel + 9) % 10)), moves + 1));
          }
        }

        -1
    }
}
