use std::collections::HashSet;

pub struct UnionFind {
    ranks: Vec<usize>,
    parents: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            ranks: vec![0; n],
            parents: (0..n).collect(),
        }
    }

    pub fn find(&mut self, mut x: usize) -> usize {
        while self.parents[x] != x {
            let temp = self.parents[self.parents[x]];
            self.parents[x] = temp;
            x = self.parents[x];
        }
        x
    }

    pub fn union(&mut self, x: usize, y: usize) {
        let xbar = self.find(x);
        let ybar = self.find(y);

        if xbar == ybar {
            return;
        }

        if self.ranks[xbar] > self.ranks[ybar] {
            self.parents[ybar] = xbar;
        } else {
            self.parents[xbar] = ybar;
            if self.ranks[xbar] == self.ranks[ybar] {
                self.ranks[ybar] += 1;
            }
        }
    }

    pub fn count_components(&mut self) -> usize {
        let mut components = HashSet::new();

        for p in &self.parents {
            components.insert(*p);
        }

        components.len()
    }
}
