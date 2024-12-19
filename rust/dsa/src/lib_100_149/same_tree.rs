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
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        if p.is_none() && q.is_none() {
            return true;
        }

        if p.is_none() || q.is_none() {
            return false;
        }

        let mut stack = vec![(p, q)];

        while let Some(pair) = stack.pop() {
            match pair {
                (None, None) => continue,
                (Some(l), Some(r)) => {
                    let lnode = l.borrow();
                    let rnode = r.borrow();

                    if lnode.val != rnode.val {
                        return false;
                    }

                    stack.push((lnode.left.clone(), rnode.left.clone()));
                    stack.push((lnode.right.clone(), rnode.right.clone()))
                }
                _ => return false,
            }
        }

        true
    }
}
