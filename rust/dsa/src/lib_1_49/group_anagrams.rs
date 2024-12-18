struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hashtbl: HashMap<String, Vec<String>> = HashMap::with_capacity(strs.len());

        for word in strs {
            let mut k: Vec<char> = word.chars().collect();
            k.sort();
            let key: String = k.into_iter().collect();
            hashtbl.entry(key).or_insert(Vec::new()).push(word);
        }

        let mut res: Vec<Vec<String>> = Vec::with_capacity(hashtbl.len());

        for val in hashtbl.into_values() {
            res.push(val);
        }

        res
    }
}
