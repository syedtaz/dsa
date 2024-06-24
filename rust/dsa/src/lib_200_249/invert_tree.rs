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

struct Solution;

use std::cell::RefCell;
use std::mem;
use std::rc::Rc;

type Tree = Option<Rc<RefCell<TreeNode>>>;

impl Solution {
    pub fn invert_tree(root: Tree) -> Tree {
        let mut stack: Vec<Tree> = vec![root.clone()];

        while let Some(outer) = stack.pop() {
          if let Some(inner) = outer {
            let TreeNode { left, right, .. } = &mut *inner.borrow_mut();
            mem::swap(right, left);
            stack.push(right.clone());
            stack.push(left.clone());
          }
        }

        root
    }
}
