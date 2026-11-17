use std::collections::{HashMap, BTreeMap};

struct TimeMap {

    storage : HashMap<String, BTreeMap<i32, String>>
}

impl TimeMap {
    fn new() -> Self {

        Self { storage : HashMap::new() }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        match self.storage.entry(key) {
            std::collections::hash_map::Entry::Occupied(mut  occupied_entry) =>{
                let btreemap = occupied_entry.get_mut();
                btreemap.insert(timestamp, value);
            },
            std::collections::hash_map::Entry::Vacant(vacant_entry) => {
                
                vacant_entry.insert(BTreeMap::from([(timestamp, value)]));
            },
        }
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        match self.storage.get(&key) {
            Some(tree) => {
                match tree.range(0..=timestamp).next_back(){
                    None => String::new(),
                    Some((_, st)) => st.clone()
                }
            },
            None => {
                String::new()
            }
        }
    }
}
