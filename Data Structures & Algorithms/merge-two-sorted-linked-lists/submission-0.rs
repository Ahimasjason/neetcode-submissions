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
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {

        let mut  dummy =  ListNode::new(-1);
        let mut prev = &mut dummy ;
        while list1.is_some() & list2.is_some() {
            
            let val = if list1.as_ref().unwrap().val < list2.as_ref().unwrap().val {
                let mut v = list1.take().unwrap();
                list1 = v.next.take();
                v
            } else {
                let mut v = list2.take().unwrap();
                list2 = v.next.take();
                v
            };
            let node = val;
            prev.next = Some(node);
            let n = prev.next.as_mut().unwrap();
            prev = n;

        }


        while list1.is_some() {
            let mut node = list1.take().unwrap();
            list1 = node.next.take();
            prev.next = Some(node);
            let n = prev.next.as_mut().unwrap();
            prev = n;
            
        }

        while list2.is_some() {
            let mut node = list2.take().unwrap();
            list2 = node.next.take();
            prev.next = Some(node);
            let n = prev.next.as_mut().unwrap();
            prev = n;
            
        }

        dummy.next.take()
    }

}
