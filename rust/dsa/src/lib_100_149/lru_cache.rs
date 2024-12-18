use std::cell::RefCell;
use std::marker::PhantomData;
use std::rc::{Rc, Weak};

struct Node {
    value: i32,
    prev: Option<Weak<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(value: i32) -> Self {
        Node {
            value,
            prev: None,
            next: None,
        }
    }

    pub fn splice(&mut self) -> Self {
      match self.prev
    }
}

struct List<'a> {
    front: Option<Rc<RefCell<Node>>>,
    back: Option<Rc<RefCell<Node>>>,
    _phantom: PhantomData<&'a i32>,
}

impl<'a> List<'a> {
    pub fn new() -> Self {
        List {
            front: None,
            back: None,
            _phantom: PhantomData,
        }
    }

    pub fn insert(list: List<'a>, value: i32) -> &'a Rc<RefCell<Node>> {


        todo!()
    }
}
