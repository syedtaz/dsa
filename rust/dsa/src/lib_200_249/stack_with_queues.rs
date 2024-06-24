#![allow(dead_code)]

use std::collections::VecDeque;

struct MyStack {
    state: VecDeque<i32>,
}

impl MyStack {
    fn new() -> Self {
        MyStack {
            state: VecDeque::new(),
        }
    }

    fn push(&mut self, x: i32) {
      self.state.push_back(x);
      let mut size = self.state.len();

      while size > 1 {
        let y = self.state.pop_front().unwrap();
        self.state.push_back(y);
        size -= 1
      }
    }

    fn pop(&mut self) -> i32 {
      self.state.pop_front().unwrap()
    }

    fn top(&self) -> i32 {
      *self.state.front().unwrap()
    }

    fn empty(&self) -> bool {
      self.state.len() == 0
    }
}
