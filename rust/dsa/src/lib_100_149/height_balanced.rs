use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub struct Solution {}

enum Continuation {
    Cont(Rc<RefCell<TreeNode>>),
    Height(usize),
}

impl Solution {
    pub fn is_balanced_recursive(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut acc: bool = true;

        fn balanced(node: &Option<Rc<RefCell<TreeNode>>>, acc: &mut bool) -> i32 {
            match node {
                None => 0,
                Some(n) => {
                    let b = n.borrow();
                    let hleft = balanced(&b.left, acc);
                    let hright = balanced(&b.right, acc);
                    let diff = hleft.abs_diff(hright) <= 1;
                    *acc = (*acc) & diff;

                    hleft.max(hright) + 1
                }
            }
        }

        balanced(&root, &mut acc);
        acc
    }

    pub fn is_balanced(mut node: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut stack = Vec::new();

        'outer: loop {
            let mut ret: usize = match node {
                None => 0,
                Some(n) => {
                    stack.push(Continuation::Cont(n.clone()));
                    node = n.borrow().left.as_ref().cloned();
                    continue;
                }
            };

            while let Some(c) = stack.pop() {
                match c {
                    Continuation::Cont(n) => {
                        stack.push(Continuation::Height(ret));
                        node = n.borrow().right.as_ref().cloned();
                        continue 'outer;
                    }
                    Continuation::Height(h) => match (ret.abs_diff(h)) <= 1 {
                        false => return false,
                        true => {
                            ret = h.max(ret) + 1;
                        }
                    },
                }
            }
            return true;
        }
    }
}
