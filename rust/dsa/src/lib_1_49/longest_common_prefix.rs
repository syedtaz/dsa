pub struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::from("");
        }

        let shortest = strs.iter().fold(strs.first().unwrap(), |acc, x| {
            if x.len() < acc.len() {
                x
            } else {
                acc
            }
        });

        let mut prefix = Vec::with_capacity(shortest.len());

        for (i, c) in shortest.chars().enumerate() {
            let mut matched = true;
            for s in strs.iter() {
                if s.as_bytes()[i] != c as u8 {
                    matched = false;
                }
            }

            if !matched {
                break;
            }

            prefix.push(c);
        }

        prefix.into_iter().collect()
    }
}
