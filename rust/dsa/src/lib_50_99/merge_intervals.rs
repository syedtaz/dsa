pub struct Solution {}

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut stack: Vec<Vec<i32>> = Vec::with_capacity(intervals.len());
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));

        for interval in intervals {
            match stack.last() {
                None => {
                    stack.push(interval);
                }
                Some(top) => {
                    let cur_x = interval[0];
                    let cur_y = interval[1];

                    let top_x = top[0];
                    let top_y = top[1];

                    match top_y < cur_x {
                        false => {
                            stack.pop();
                            stack.push(vec![cur_x.min(top_x), top_y.max(cur_y)])
                        }
                        true => stack.push(vec![cur_x, cur_y]),
                    }
                }
            }
        }

        stack
    }
}
