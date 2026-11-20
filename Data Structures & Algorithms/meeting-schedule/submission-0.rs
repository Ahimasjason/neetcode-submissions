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
    pub fn can_attend_meetings(mut intervals: Vec<Interval>) -> bool {
        intervals.sort_by(|int1, int2| int1.start.cmp(&int2.start));
        let mut idx = 1;
        while idx < intervals.len() {
            if intervals[idx].start <  intervals[idx -1].end {
                return false
            }
            idx += 1;
        }

        true
    }
}
