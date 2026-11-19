impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        const START : usize = 0;
        const END : usize = 1;
        // let mut int = intervals;
        intervals.sort_by(|l,r| l[START].cmp(&r[START]) ) ;
        let mut op: Vec<Vec<i32>> = vec![];

        for int in intervals {

            if op.len() > 0 && int[START] <= op[op.len() -1][END]{
                let last = op.pop().unwrap();
                let new = vec![last[START].min(int[START]) , last[END].max(int[END])];
                op.push(new);
            } else {
                op.push(int);
            }   
        }
        op 

    }
}
