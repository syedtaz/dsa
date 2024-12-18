struct MyCircularQueue {
    buffer: Vec<i32>,
    front: usize,
    back: usize,
    len: usize,
}

impl MyCircularQueue {
    fn new(k: i32) -> Self {
        MyCircularQueue {
            buffer: vec![0; k as usize],
            front: 0,
            back: 0,
            len: 0,
        }
    }

    fn en_queue(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }

        self.buffer[self.back] = value;
        self.len += 1;
        self.back += 1;
        self.back = self.back % self.buffer.capacity();
        true
    }

    fn de_queue(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }

        println!("{:?}", self.buffer);
        self.front += 1;
        self.front = self.front % self.buffer.capacity();
        self.len -= 1;
        true
    }

    fn front(&mut self) -> i32 {
        if self.is_empty() {
            return -1;
        }

        self.buffer[self.front]
    }

    fn rear(&self) -> i32 {
        if self.is_empty() {
            return -1;
        }

        if self.back == 0 {
            return self.buffer[self.buffer.len() - 1];
        }

        self.buffer[self.back - 1]
    }

    fn is_empty(&self) -> bool {
        self.len == 0
    }

    fn is_full(&self) -> bool {
        println!("{:?}", self.buffer.capacity());
        self.len == self.buffer.capacity()
    }
}