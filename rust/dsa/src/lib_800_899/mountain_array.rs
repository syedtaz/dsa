use std::cmp::Ordering;

pub struct Solution {}

impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = arr.len() - 1;

        while (j - i) != 2 {
            let m = i + (j - i) / 2;
            match arr[m].cmp(&arr[i]) {
                Ordering::Greater | Ordering::Equal => i = m,
                Ordering::Less => {
                    j = m;
                }
            }
        }

        (j - i + 1) as i32
    }
}
