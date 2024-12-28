pub struct Solution {}

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
}

impl Solution {
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        if (connections.len() as i32) < n - 1 {
            return -1;
        }

        let mut uf = UnionFind::new(n as usize);
        let mut ncomp = n;

        for conn in &connections {
            let left = conn[0] as usize;
            let right = conn[1] as usize;
            if uf.find(left) != uf.find(right) {
                uf.union(left, right);
                ncomp -= 1;
            }
        }

        ncomp - 1
    }
}
