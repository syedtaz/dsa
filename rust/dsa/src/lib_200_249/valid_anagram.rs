use std::collections::HashMap;

struct Solution;

impl Solution {
    fn generate_counter(s: String) -> HashMap<char, u32> {
        s.chars()
            .into_iter()
            .fold(HashMap::with_capacity(s.len()), |mut acc, c| {
                *acc.entry(c).or_insert(0) += 1;
                acc
            })
    }

    pub fn is_anagram(s: String, t: String) -> bool {
        Solution::generate_counter(s).eq(&Solution::generate_counter(t))
    }
}
