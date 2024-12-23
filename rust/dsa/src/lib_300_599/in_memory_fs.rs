use std::collections::BTreeMap;

pub enum File<'a> {
    F(String),
    D(BTreeMap<&'a str, File<'a>>),
}

use File::*;

pub struct FileSystem<'a> {
    root: File<'a>,
}

impl<'a> FileSystem<'a> {
    fn new() -> Self {
        FileSystem {
            root: D(BTreeMap::new()),
        }
    }

    fn traverse(&'a mut self, path: String, create: bool) -> Option<&'a mut File<'a>> {
        let mut cur = &mut self.root;
        let chunks = path.split("/").filter(|x| *x != "");

        for node in chunks {
            match cur {
                F(_) => {
                    return None;
                }
                D(dir) => {
                    if !dir.contains_key(node) && !create {
                        return None;
                    }
                    cur = dir.entry(node).or_insert(D(BTreeMap::new()));
                }
            }
        }

        Some(cur)
    }

    pub fn ls(&'a mut self, path: String) -> Vec<String> {
        match self.traverse(path, false) {
            None => Vec::new(),
            Some(F(f)) => {
                vec![f.clone()]
            }
            Some(D(dir)) => {
                let mut res = Vec::with_capacity(dir.len());
                for k in dir.keys() {
                    res.push(k.clone().to_string())
                }
                res
            }
        }
    }
}
