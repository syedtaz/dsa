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
    pub fn is_palindrome(mut head: Option<Box<ListNode>>) -> bool {
        // Find midpoint

        let mut length = 0;
        let mut cur = &head;
        while let Some(i) = cur {
            length += 1;
            cur = &i.next
        }

        // Reverse second half in place

        let mut tail = &mut head;
        for _ in 0..(length - 1) / 2 {
            tail = &mut tail.as_mut().unwrap().next;
        }

        let mut prev = None;
        let mut cur = tail.as_mut().unwrap().next.take();

        while let Some(mut node) = cur {
            cur = node.next;
            node.next = prev;
            prev = Some(node);
        }

        let mut right = &prev;
        let mut left = &head;

        while let (Some(l), Some(r)) = (left, right) {
            if l.val != r.val {
                return false;
            }
            right = &r.next;
            left = &l.next;
        }

        true
    }
}
