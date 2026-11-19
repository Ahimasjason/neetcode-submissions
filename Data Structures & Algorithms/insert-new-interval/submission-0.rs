impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {

        const START : usize = 0;
        const END : usize = 1;
        let mut op = vec![];

        let mut ii = 0;
    
        while ii < intervals.len() &&  intervals[ii][END] < new_interval[START] {
            // println!("LESS {:?}", op);
            op.push(vec![intervals[ii][START], intervals[ii][END]]);
            ii += 1;
        }

        op.push(new_interval);
        // we are in the overlapping phase
        
        while ii < intervals.len() && intervals[ii][START] <= op[op.len() - 1][END]  {
            // println!("OVERLAP {:?}", op);
            let last_int = op.pop().unwrap();
            let nv = vec![last_int[START].min(intervals[ii][START]), last_int[END].max(intervals[ii][END])];
            op.push(nv);
            ii+=1;
        }

        while ii < intervals.len() {
            // println!("GREATER {:?}", op);
            op.push(vec![intervals[ii][START], intervals[ii][END]]);
            ii += 1;
        }
        op
    }
}
