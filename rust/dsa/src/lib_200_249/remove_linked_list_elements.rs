#![allow(dead_code)]

struct Solution;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn remove_elements(mut head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut sentinel = None;
        let mut curr = &mut sentinel;

        while let Some(mut x) = head.take() {
            head = x.next.take();
            if x.val != val {
                curr = &mut curr.insert(x).next;
            }
        }

        sentinel
    }
}

// let mut lst = None;
// let mut tail = &mut lst;

// while let Some(mut x) = head.take() {
//   head = x.next.take();

//   if x.val != val {
//     tail = &mut tail.insert(x).next;
//   }
// }

// lst
