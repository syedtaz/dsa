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

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut acc = 0;

        fn f(node: &Option<Rc<RefCell<TreeNode>>>, acc: &mut i32) -> i32 {
            match node {
                None => 0,
                Some(n) => {
                    let left = f(&n.borrow().left, acc);
                    let right = f(&n.borrow().right, acc);
                    let m = left.max(right);
                    *acc = (*acc).max(m + 1);

                    m + 1
                }
            }
        }

        f(&root, &mut acc);
        acc
    }
}
