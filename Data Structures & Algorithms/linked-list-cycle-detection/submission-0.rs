// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: *mut ListNode,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: std::ptr::null_mut(), val }
//     }
// }

impl Solution {
    pub fn has_cycle(head: *mut ListNode) -> bool {
       unsafe {
        if head.is_null() {return false}
        let mut sp = head;
        let mut fp = head;
        while !fp.is_null() && !(*fp).next.is_null() {
            sp   = (*sp).next;
            
            fp = (*(*fp).next).next;
            if sp == fp { return  true;}
        }
        
    }
    
    false
    }
}
