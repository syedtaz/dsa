#![allow(dead_code)]

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

struct Solution;

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref()?.next.is_none() {
            return head;
        }

        let mut sentinel = head;
        let mut i = sentinel.as_mut().unwrap();

        while let Some(j) = i.next.as_mut() {
            if j.val == i.val {
                i.next = j.next.take();
            } else {
                i = i.next.as_mut().unwrap();
            }
        }

        sentinel
    }
}
