pub struct Solution {}

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack = Vec::new();

        for p in path.split("/") {
            match p {
                "." | "/" | "" => continue,
                ".." => {
                    if !stack.is_empty() {
                        stack.pop();
                    };
                }
                _ => {
                    stack.push(p.to_string());
                }
            }
        }
        println!("{:?}", stack);

        let mut res = String::from("/");
        res.push_str(&stack.join("/"));
        res
    }
}
