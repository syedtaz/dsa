pub struct Peterson {
    flag: [bool; 2],
    victim: usize,
}

impl Peterson {
    pub fn lock(&mut self, i: usize) -> () {
        if i != 0 || i != 1 {
            panic!()
        }

        let j = 1 - i;
        self.flag[i] = true;
        self.victim = i;
        loop {
            if !flag[j] || victim != i {
                break;
            }
        }
    }

    pub fn unlock(&mut self, i: usize) -> () {
        self.flag[i] = false;
    }
}
