#![allow(dead_code)]

struct Solution;

use std::collections::HashMap;

#[derive(Debug)]
struct Node {
    value: char,
    word: bool,
    children: HashMap<char, Node>,
}

impl Node {
    pub fn new(ch: char) -> Self {
        Node {
            value: ch,
            word: false,
            children: HashMap::new(),
        }
    }
}

#[derive(Debug)]
struct Trie {
    root: Node,
}

impl Trie {
    pub fn new() -> Self {
        Trie {
            root: Node::new('\0'),
        }
    }

    pub fn insert(&mut self, word: &str) -> () {
        let mut curr = &mut self.root;

        for ch in word.chars().into_iter() {
            if !curr.children.contains_key(&ch) {
                let _ = curr.children.insert(ch, Node::new(ch));
            }
            curr = curr.children.get_mut(&ch).unwrap();
        }

        curr.word = true;
    }

    pub fn prefix(&self, word: &String) -> i32 {
        let mut curr = &self.root;
        let mut acc: i32 = 0;

        for ch in word.chars().into_iter() {
            if curr.children.len() != 1 {
                return acc;
            }
            curr = curr.children.get(&ch).unwrap();
            acc += 1
        }

        acc
    }
}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut trie = Trie::new();
        for word in strs.iter() {
            if word == "" {
                return "".to_string();
            }
            trie.insert(word)
        }

        let shortest = strs
            .iter()
            .reduce(|acc, e| if acc.len() <= e.len() { acc } else { e })
            .unwrap()
            .len();

        let choices: Vec<&String> = strs.iter().filter(|x| x.len() == shortest).collect();

        let (_, res) = choices.iter().fold((0, ""), |(length, prev), e| {
            let l = trie.prefix(e);
            if l > length {
                (l, e)
            } else {
                (length, prev)
            }
        });

        res.to_string()
    }
}
