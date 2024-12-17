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
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut length = 0;
        let mut cur = &head;

        while let Some(i) = cur {
            length += 1;
            cur = &i.next;
        }

        let mut cursor = head;
        for _ in 0..(length) / 2 {
            cursor = cursor.unwrap().next
        }

        cursor
    }
}
