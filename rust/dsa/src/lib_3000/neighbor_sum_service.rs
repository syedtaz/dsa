use std::collections::HashMap;

struct NeighborSum {
    memo: HashMap<i32, (i32, i32)>,
}

impl NeighborSum {
    fn new(grid: Vec<Vec<i32>>) -> Self {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;
        let adj_d = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];
        let diag_d = vec![(-1, 1), (-1, -1), (1, 1), (1, -1)];

        let mut memo: HashMap<i32, (i32, i32)> = HashMap::with_capacity(m as usize * n as usize);

        for (i, row) in grid.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                let mut adj = 0;
                for (dx, dy) in adj_d.iter() {
                    if (0 <= i as i32 + *dx)
                        && (i as i32 + *dx < m)
                        && (0 <= j as i32 + *dy)
                        && (j as i32 + *dy < n)
                    {
                        adj += grid[i + (*dx) as usize][j + (*dy) as usize]
                    }
                }

                let mut diag = 0;
                for (dx, dy) in diag_d.iter() {
                    if (0 <= i as i32 + *dx)
                        && (i as i32 + *dx < m)
                        && (0 <= j as i32 + *dy)
                        && (j as i32 + *dy < n)
                    {
                        diag += grid[i + (*dx) as usize][j + (*dy) as usize]
                    }
                }

                memo.insert(*val, (adj, diag));
            }
        }

        Self { memo }
    }

    fn adjacent_sum(&self, value: i32) -> i32 {
        self.memo.get(&value).unwrap().0
    }

    fn diagonal_sum(&self, value: i32) -> i32 {
        self.memo.get(&value).unwrap().1
    }
}
