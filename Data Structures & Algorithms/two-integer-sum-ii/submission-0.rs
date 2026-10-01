impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {


        let (mut start, mut end ) = (0, numbers.len() - 1);

        while start < end {

            let sum = numbers[start] + numbers[end];

            if sum > target {
                end -= 1;
            } else if sum < target {
                start += 1
            } else {
                return vec![start as i32 + 1, end as i32 + 1]
            }
        }

        vec![]

    }
}
