#![allow(dead_code)]

struct Solution;

use std::borrow::BorrowMut;
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

type Node = Rc<RefCell<TreeNode>>;

impl Solution {
    pub fn inorder_traversal(root: Option<Node>) -> Vec<i32> {
        let mut acc: Vec<i32> = Vec::new();
        let mut curr = root;

        // while curr.is_some() {
        //   let cnode = curr.as_ref().unwrap().as_ref().borrow_mut();

        //   if cnode.left.is_none() {
        //     acc.push(cnode.val);
        //     curr = cnode.right;
        //   };
        // }

        acc
    }
}
