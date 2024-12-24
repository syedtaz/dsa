use std::collections::BinaryHeap;

struct KthLargest {
    k: usize,
    state: BinaryHeap<i32>,
}

impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut _self = KthLargest {
            k: k as usize,
            state: BinaryHeap::with_capacity(k as usize + 1),
        };

        for num in nums {
            _self.add(num);
        }

        _self
    }

    fn add(&mut self, val: i32) -> i32 {
        self.state.push(-val);
        if self.state.len() > self.k {
            self.state.pop();
        }
        -1 * *self.state.peek().unwrap()
    }
}
