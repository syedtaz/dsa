pub struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::with_capacity(nums2.len());
        let mut map: HashMap<i32, i32> = HashMap::new();

        for i in nums2 {
            while !stack.is_empty() {
                match stack.last() {
                    Some(x) if i > *x => {
                        let k = stack.pop().unwrap();
                        map.insert(k, i);
                    }
                    None | Some(_) => break,
                }
            }
            stack.push(i);
        }

        for i in stack {
            map.insert(i, -1);
        }

        nums1.into_iter().map(|x| *map.get(&x).unwrap()).collect()
    }
}
