#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {
        if intervals.len() == 0 || intervals.len() == 1 {
            return true;
        }

        intervals.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
        intervals
            .iter()
            .zip(intervals.iter().skip(1))
            .all(|(a, b)| a[1] <= b[0])
    }
}
