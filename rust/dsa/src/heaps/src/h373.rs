pub struct Solution {}

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

impl Solution {
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::with_capacity(k as usize * 2);
        let mut ans = Vec::with_capacity(k as usize);
        heap.push((Reverse(nums1[0] + nums2[0]), 0, 0));
        let mut target = k;

        let mut seen = HashSet::with_capacity(k as usize * 2);

        while let Some((_, i, j)) = heap.pop() {
            if target <= 0 {
                break;
            }

            ans.push(vec![nums1[i], nums2[j]]);
            target -= 1;

            if i + 1 < nums1.len() && !seen.contains(&(i + 1, j)) {
                seen.insert((i + 1, j));
                heap.push((Reverse(nums1[i + 1] + nums2[j]), i + 1, j));
            }

            if j + 1 < nums2.len() && !seen.contains(&(i, j + 1)) {
                seen.insert((i, j + 1));
                heap.push((Reverse(nums1[i] + nums2[j + 1]), i, j + 1));
            }
        }

        ans
    }
}
