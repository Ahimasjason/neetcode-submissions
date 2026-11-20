/**
 * Definition of Interval:
 * #[derive(Debug, Clone)]
 * pub struct Interval {
 *     pub start: i32,
 *     pub end: i32,
 * }
 *
 * impl Interval {
 *     pub fn new(start: i32, end: i32) -> Self {
 *         Interval { start, end }
 *     }
 * }
 */

impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Interval>) -> i32 {
        
        let mut counter = 0;
        let (mut start, mut end) : (Vec<_>, Vec<_>)= intervals.into_iter().map(|int| (int.start , int.end)).unzip();
        start.sort();
        end.sort();
        let mut ans = 0;
        let mut si  = 0;
        let mut ei = 0;
        while ei < start.len() && si < start.len() {
            let st = start[si];
            let ed = end[ei];
            if st < ed {
                counter+=1;
                ans = ans.max(counter);
                si += 1;
            } else  {
                ei += 1;
                counter -= 1;

            } 
        }
        ans
    }
}
