pub struct Solution {}

pub struct UnionFind {
    ranks: Vec<usize>,
    pub parents: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            ranks: vec![0; n],
            parents: (0..n).collect(),
        }
    }

    pub fn find(&mut self, mut n: usize) -> usize {
        while self.parents[n] != n {
            let temp = self.parents[self.parents[n]];
            self.parents[n] = temp;
            n = self.parents[n];
        }
        n
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

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn construct_uf(grid: &[Vec<i32>]) -> UnionFind {
        let m = grid.len();
        let n = grid[0].len();
        let mut uf = UnionFind::new(m * n);
        let deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)];

        for (i, row) in grid.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                if *val == 0 {
                    continue;
                }

                let cur = i * n + j;

                for (di, dj) in &deltas {
                    let x = (i as i32) + di;
                    let y = (j as i32) + dj;
                    if 0 <= x
                        && x < m as i32
                        && 0 <= y
                        && y < n as i32
                        && grid[x as usize][y as usize] == 1
                    {
                        uf.union(cur, (x as usize) * n + y as usize);
                    }
                }
            }
        }

        // Force path compression
        for i in 0..(m * n) {
            uf.find(i);
        }

        uf
    }

    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {
        let mut uf = Solution::construct_uf(&grid2);
        let m = grid2.len();
        let n = grid2[0].len();
        let mut subisland = vec![true; m * n];

        for (i, row) in grid2.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                if *val == 1 && grid1[i][j] != 1 {
                    subisland[uf.find(i * n + j)] = false;
                }
            }
        }

        let mut acc = 0;
        for (i, row) in grid2.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                if *val == 1 {
                    let parent = uf.find(i * n + j);
                    if subisland[parent] {
                        subisland[parent] = false;
                        acc += 1;
                    }
                }
            }
        }

        acc
    }
}
