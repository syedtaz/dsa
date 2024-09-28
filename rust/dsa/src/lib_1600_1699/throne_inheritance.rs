use std::collections::{HashMap, HashSet};

struct ThroneInheritance {
    children: HashMap<String, Vec<String>>,
    dead: HashSet<String>,
    king: String,
}

impl ThroneInheritance {
    fn new(kingName: String) -> Self {
        ThroneInheritance {
            children: HashMap::from([(kingName.clone(), Vec::new())]),
            dead: HashSet::new(),
            king: kingName,
        }
    }

    fn birth(&mut self, parent_name: String, child_name: String) {
        self.children
            .get_mut(&parent_name)
            .unwrap()
            .push(child_name.clone());
        self.children.insert(child_name, Vec::new());
    }

    fn death(&mut self, name: String) {
        self.dead.insert(name);
    }

    fn get_inheritance_order(&self) -> Vec<String> {
        let mut acc: Vec<String> = Vec::new();
        let mut stack: Vec<&String> = vec![&self.king];

        while let Some(person) = stack.pop() {
            if !(self.dead.contains(person)) {
                acc.push(person.clone());
            }

            for child in self.children.get(person).unwrap().iter().rev() {
                stack.push(child);
            }
        }

        acc
    }
}
