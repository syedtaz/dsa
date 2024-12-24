pub struct Solution {}

use std::collections::HashMap;

pub fn convert(w: &str) -> Vec<(usize, usize)> {
    let mapping: HashMap<char, usize> = w.chars().into_iter().enumerate().fold(
        HashMap::with_capacity(w.len()),
        |mut acc, (i, x)| match acc.get(&x) {
            None => {
                acc.insert(x, i);
                acc
            }
            Some(_) => acc,
        },
    );

    let mut res: Vec<(usize, usize)> = w
        .chars()
        .into_iter()
        .fold(HashMap::with_capacity(w.len()), |mut acc, x| {
            *acc.entry(x).or_insert(0) += 1;
            acc
        })
        .into_iter()
        .map(|(k, v)| (*mapping.get(&k).unwrap(), v))
        .collect();
    res.sort();

    res
}

impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        let pat = convert(&pattern);
        words
            .iter()
            .map(|x| (convert(x), x))
            .filter(|(x, _)| *x == pat)
            .map(|(_, x)| x.clone())
            .collect()
    }
}
