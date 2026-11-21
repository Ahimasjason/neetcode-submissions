// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn reverse_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {

        
        let mut prev = None;

        while head.is_some() {

            let mut n = head.unwrap(); // ListNode {val , Option<Box<ListNode>>}
            let next = n.next.take(); // Option<Box<LN>>
            n.next = prev;
            prev = Some(n);
            head = next;

        }
        prev
    }
}
