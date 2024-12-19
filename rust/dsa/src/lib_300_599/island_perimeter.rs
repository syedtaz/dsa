pub struct Solution {}

impl Solution {
  pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
    let mut res = 0;

    for (i, row) in grid.iter().enumerate() {
      for (j, val) in row.iter().enumerate() {
        if *val == 1 {
          res += 4;
          if i > 0 && grid[i - 1][j] == 1 {
            res -= 2;
          }
          if j > 0 && grid[i][j - 1] == 1 {
            res -= 2;
          }
        }
      }
    }

    res
  }
}