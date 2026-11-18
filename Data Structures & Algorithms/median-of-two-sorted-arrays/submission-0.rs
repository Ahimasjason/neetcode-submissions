impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        use std::collections::BinaryHeap;
        use std::cmp::Reverse;

        let mut max_heap = BinaryHeap::new();
        let mut min_heap = BinaryHeap::new();
        let is_div_by_2 = (nums1.len() + nums2.len()).is_multiple_of(2);
        for v in nums1.into_iter().chain(nums2.into_iter()) {
            max_heap.push(v);
            min_heap.push(Reverse(max_heap.pop().unwrap()));
            if min_heap.len() > max_heap.len() + 1 {
                max_heap.push(min_heap.pop().unwrap().0)
            }
        }
        // println!("max_heap = {:?}\nmin_heap={:?}", max_heap, min_heap);
        if !is_div_by_2{
            (min_heap.peek().unwrap().0 )as f64
        } else {
            let first = *max_heap.peek().unwrap() as f64;
            let second = min_heap.peek().unwrap().0  as f64;
            (first + second) /2.0
        }
    }
}
