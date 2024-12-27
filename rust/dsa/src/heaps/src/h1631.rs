pub struct Solution {}

use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn within_bound(
    x: usize,
    y: usize,
    dx: i32,
    dy: i32,
    m: usize,
    n: usize,
) -> Option<(usize, usize)> {
    let xp = x as i32 + dx;
    let yp = y as i32 + dy;
    if 0 <= xp && xp < m as i32 && 0 <= yp && yp < n as i32 {
        Some((xp as usize, yp as usize))
    } else {
        None
    }
}

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        // Initialize SSSP
        let m = heights.len();
        let n = heights[0].len();
        let mut visited = vec![vec![false; n]; m];
        let mut dist = vec![vec![u32::MAX; n]; m];
        dist[0][0] = 0;

        // Initalize heap
        let mut heap = BinaryHeap::with_capacity(m * n);
        heap.push((Reverse(0), (0, 0)));

        let deltas = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

        while let Some((Reverse(cost), (x, y))) = heap.pop() {
            if x == m - 1 && y == n - 1 {
                return i32::try_from(cost).unwrap();
            }

            visited[x][y] = true;

            for (dx, dy) in &deltas {
                if let Some((xp, yp)) = within_bound(x, y, *dx, *dy, m, n) {
                    if visited[xp][yp] {
                        continue;
                    }

                    let diff = heights[x][y].abs_diff(heights[xp][yp]);
                    let mdiff = diff.max(dist[x][y]);
                    if dist[xp][yp] > mdiff {
                        dist[xp][yp] = mdiff;
                        heap.push((Reverse(mdiff), (xp, yp)));
                    }
                }
            }
        }

        i32::try_from(dist[m - 1][n - 1]).unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn example1() {
        let heights = vec![vec![1, 2, 2], vec![3, 8, 2], vec![5, 3, 5]];
        assert_eq!(Solution::minimum_effort_path(heights), 2);
    }

    #[test]
    fn example2() {
        let heights = vec![vec![1, 2, 3], vec![3, 8, 4], vec![5, 3, 5]];
        assert_eq!(Solution::minimum_effort_path(heights), 1);
    }

    #[test]
    fn example3() {
        let heights = vec![
            vec![1, 2, 1, 1, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 1, 1, 2, 1],
        ];
        assert_eq!(Solution::minimum_effort_path(heights), 0);
    }
}
