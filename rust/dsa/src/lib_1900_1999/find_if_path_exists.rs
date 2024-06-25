#![allow(dead_code)]

use std::cmp::Ordering::{Equal, Greater, Less};
use std::collections::HashMap;

struct Solution;

struct UnionFind {
    parents: HashMap<i32, i32>,
    ranks: HashMap<i32, usize>,
}

impl UnionFind {
    pub fn new(n: i32) -> Self {
        UnionFind {
            parents: (0..n).into_iter().map(|x| (x, x)).collect(),
            ranks: (0..n).into_iter().map(|x| (x, 0)).collect(),
        }
    }

    pub fn find(&mut self, a: i32) -> i32 {
        let parent = *self.parents.get(&a).unwrap();
        if parent != a {
            let res = self.find(parent);
            let _ = self.parents.insert(a, res);
        }

        *self.parents.get(&a).unwrap()
    }

    pub fn union(&mut self, x: i32, y: i32) -> () {
        let xbar = self.find(x);
        let ybar = self.find(y);

        if xbar == ybar {
            return;
        }

        let xbar_rank = self.ranks.get(&xbar).unwrap();
        let ybar_rank = self.ranks.get(&ybar).unwrap();

        match xbar_rank.cmp(ybar_rank) {
            Greater => {
                let _ = self.parents.insert(ybar, xbar);
            }
            Equal => {
                let _ = self.parents.insert(xbar, ybar);
                *self.ranks.get_mut(&ybar).unwrap() += 1;
            }
            Less => {
                let _ = self.parents.insert(xbar, ybar);
            }
        }
    }
}

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let mut uf = UnionFind::new(n);

        for lst in edges.iter() {
            let a = lst[0];
            let b = lst[1];
            uf.union(a, b);
        }

        for x in (0..n).into_iter() {
            let _ = uf.find(x);
        }

        uf.find(source) == uf.find(destination)
    }
}
