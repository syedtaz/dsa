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
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
      if root.is_none() {
        return false;
      }

      let mut stack = vec![(root, 0)];
      while let Some((nnode, val)) = stack.pop() {
        match nnode {
          None => continue,
          Some(node) => {
            let nval = node.borrow().val + val;

            if node.borrow().left.is_none() && node.borrow().right.is_none() {
              match nval == target_sum {
                true => { return true; }
                false => continue
              }
            }

            stack.push((node.borrow().left.clone(), nval));
            stack.push((node.borrow().right.clone(), nval))
          }
        }
      }

      false
    }
}
