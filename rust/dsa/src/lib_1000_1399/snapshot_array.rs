struct SnapshotArray {
    state: Vec<i32>,
    archive: Vec<Vec<i32>>,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        SnapshotArray {
            state: vec![0; length as usize],
            archive: Vec::with_capacity(16),
        }
    }

    fn set(&mut self, index: i32, val: i32) {
      self
    }

    // fn snap(&self) -> i32 {}

    // fn get(&self, index: i32, snap_id: i32) -> i32 {}
}
