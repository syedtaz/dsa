#![allow(dead_code)]

struct MyQueue {
    front: Vec<i32>,
    back: Vec<i32>,
}

impl MyQueue {
    fn new() -> Self {
        MyQueue {
            front: Vec::new(),
            back: Vec::new(),
        }
    }

    fn rebalance(&mut self) {
        if self.front.is_empty() {
            while !self.back.is_empty() {
                self.front.push(self.back.pop().unwrap());
            }
        }
    }

    fn push(&mut self, x: i32) {
        self.back.push(x);
    }

    fn pop(&mut self) -> i32 {
        self.rebalance();
        self.front.pop().unwrap()
    }

    fn peek(&mut self) -> i32 {
        self.rebalance();
        *self.front.last().unwrap()
    }

    fn empty(&self) -> bool {
        self.front.is_empty() && self.back.is_empty()
    }
}
