pub struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mapping: HashMap<char, usize> =
            order
                .chars()
                .enumerate()
                .fold(HashMap::new(), |mut acc, (i, x)| {
                    acc.insert(x, i);
                    acc
                });

        fn f<'a>(x: &char, mapping: &'a HashMap<char, usize>) -> &'a usize {
            mapping.get(x).or(Some(&27)).unwrap()
        }

        let mut buffer: Vec<char> = s.chars().collect();
        buffer.sort_by(|a, b| f(a, &mapping).cmp(f(b, &mapping)));

        buffer.into_iter().collect()
    }
}
