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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            None => true,
            Some(r) => {
                let rx = r.borrow();
                let mut stack = vec![(rx.left.clone(), rx.right.clone())];

                while let Some(tup) = stack.pop() {
                    match tup {
                        (None, None) => continue,
                        (Some(n1), Some(n2)) => {
                            let b1 = n1.borrow();
                            let b2 = n2.borrow();
                            if b1.val != b2.val {
                                return false;
                            }

                            stack.push((b1.left.clone(), b2.right.clone()));
                            stack.push((b1.right.clone(), b2.left.clone()));
                        }
                        _ => return false,
                    }
                }

                true
            }
        }
    }
}
