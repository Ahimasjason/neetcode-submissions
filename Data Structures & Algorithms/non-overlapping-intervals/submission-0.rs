impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {

        const START: usize = 0;
        const END  : usize  =1 ;

        // intervals.sort_by(|l,r| l[START].cmp(&r[START]));
        intervals.sort_unstable();

        let mut rv = 0;
        
        let mut i = 1;
        let mut prev = intervals[0][END];
        while i < intervals.len() {

            if intervals[i][START] <  prev   {
                rv += 1;
                prev = prev.min(intervals[i][END]);
            }else {
                prev = intervals[i][END]
            }

            i+= 1;
        }

        rv
    }
}
