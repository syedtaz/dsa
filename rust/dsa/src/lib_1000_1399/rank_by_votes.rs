pub struct Solution {}

use std::cmp::Ordering;
use std::collections::HashMap;

#[derive(PartialOrd, PartialEq, Eq)]
pub struct Ranking {
    count: [usize; 26],
    name: char,
}

impl Ranking {
    pub fn new(name: char) -> Self {
        Ranking {
            count: [0; 26],
            name: name,
        }
    }
}

impl Ord for Ranking {
    fn cmp(&self, other: &Ranking) -> Ordering {
        for i in 0..26 {
            let res = self.count[i].cmp(&other.count[i]);
            match res {
                Ordering::Equal => {
                    continue;
                }
                Ordering::Less | Ordering::Greater => return res,
            }
        }

        other.name.cmp(&self.name)
    }
}

impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        let mut hashtbl: HashMap<char, Ranking> = HashMap::with_capacity(26);

        for vote in votes {
            for (i, c) in vote.chars().enumerate() {
                let handle = hashtbl.entry(c).or_insert(Ranking::new(c));
                handle.count[i] += 1;
            }
        }

        let mut results: Vec<Ranking> = hashtbl.into_iter().map(|(_k, v)| v).collect();
        results.sort_by(|a, b| b.cmp(&a));
        results.into_iter().map(|x| x.name).collect()
    }
}
