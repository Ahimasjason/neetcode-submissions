impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {


        let mut max_storage = -1;

        let (mut start, mut end) =  (0, heights.len() -1 );

        while (start < end ) {


            let width =  end - start ;
            let lh = heights[start];
            let rh = heights[end];
            let min_height = lh.min(rh);
            max_storage = max_storage.max( width as i32 * min_height);
            if lh > rh {
                end -= 1;
            } else {
                start += 1
            }

        }



        max_storage

    }
}
