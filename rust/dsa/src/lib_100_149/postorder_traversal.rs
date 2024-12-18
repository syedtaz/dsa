use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline(always)]
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
    fn fold(node: &Option<Rc<RefCell<TreeNode>>>, acc: Vec<i32>) -> Vec<i32> {
        match node {
            None => acc,
            Some(n) => {
                let x = n.borrow();
                let mut left = Solution::fold(&x.left, acc.clone());
                let right = Solution::fold(&x.right, acc.clone());
                left.extend(right);
                left.push(x.val);
                left
            }
        }
    }

    pub fn postorder_traversal_unoptimized(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        Solution::fold(&root, Vec::new())
    }

    pub fn postorder_traversal(mut root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = Vec::new();

        if root.is_none() {
            return res;
        }

        let mut prev = None;
        let mut stack = Vec::new();

        loop {
            if root.is_none() && stack.is_empty() {
                break;
            }

            if let Some(ref mut n) = root {
                let owned = n.to_owned();
                let left = n.borrow_mut().left.take();
                stack.push(owned);
                root = left;
            } else {
                let node = stack.last().unwrap();

                if node.borrow().right.is_none() || std::ptr::eq(&node.borrow().right, &prev) {
                    res.push(node.borrow().val);
                    let owned = stack.pop();
                    prev = owned;
                    root = None;
                } else {
                    let right = node.borrow_mut().right.take();
                    root = right;
                }
            }
        }

        res
    }
}
