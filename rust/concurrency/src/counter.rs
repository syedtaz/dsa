use std::sync::{Arc, Mutex};

pub struct Counter {
    lock: Mutex<i64>,
}

impl Counter {
    fn new(i: i64) -> Self {
        Counter {
            lock: Mutex::new(i),
        }
    }

    fn get_and_increment(&mut self) -> i64 {
        let temp;
        {
            let mut handle = self.lock.lock().unwrap();
            temp = *handle;
            *handle += 1;
        }
        // handle dropped and so is the lock
        temp
    }
}
