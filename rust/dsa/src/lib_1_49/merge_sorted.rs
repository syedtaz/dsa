#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

pub struct Solution {}

impl Solution {
    pub fn merge_two_lists_unoptimized(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut sentinel = ListNode::new(0);
        let mut cur = &mut sentinel;
        let mut l = list1;
        let mut r = list2;

        loop {
            match (l.is_some(), r.is_some()) {
                (true, true) => {
                    let a = l.as_ref().unwrap().val;
                    let b = r.as_ref().unwrap().val;
                    if a <= b {
                        let mut handle = l.unwrap();
                        let next = handle.next;
                        handle.next = None;
                        cur.next = Some(handle);
                        l = next;
                    } else {
                        let mut handle = r.unwrap();
                        let next = handle.next;
                        handle.next = None;
                        cur.next = Some(handle);
                        r = next;
                    }
                    cur = cur.next.as_mut().unwrap();
                }
                (true, false) => {
                    cur.next = l;
                    break;
                }
                (false, true) => {
                    cur.next = r;
                    break;
                }
                (false, false) => {
                    break;
                }
            }
        }

        sentinel.next
    }

    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut curr = &mut list1;
        while list2.is_some() {
            if curr.is_none() || list2.as_ref().unwrap().val < curr.as_ref().unwrap().val {
                std::mem::swap(curr, &mut list2);
            }
            curr = &mut curr.as_mut().unwrap().next;
        }
        list1
    }
}
