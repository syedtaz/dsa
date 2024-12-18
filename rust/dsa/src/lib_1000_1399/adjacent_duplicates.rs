pub struct Solution {}

impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut stack: Vec<char> = Vec::with_capacity(s.len());

        for c in s.chars() {
            match stack.last() {
                Some(x) if *x == c => _ = stack.pop(),
                None | Some(_) => stack.push(c),
            }
        }

        stack.into_iter().collect()
    }
}
