pub struct Solution {}

use std::collections::BinaryHeap;

impl Solution {
    pub fn min_meeting_rooms(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));

        let mut count = 0;
        let mut heap = BinaryHeap::with_capacity(intervals.len());

        for pair in intervals {
            if heap.is_empty() {
                heap.push(-pair[1]);
                count = count.max(heap.len());
                continue;
            }

            match heap.peek() {
                Some(v) if -pair[0] <= *v => {
                    heap.pop();
                }
                _ => {}
            }

            heap.push(-pair[1]);
            count = count.max(heap.len());
        }

        i32::try_from(count).unwrap()
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(
            Solution::min_meeting_rooms(vec![vec![0, 30], vec![5, 10], vec![15, 20]]),
            2
        );
    }

    #[test]
    fn example2() {
        assert_eq!(
            Solution::min_meeting_rooms(vec![vec![7, 10], vec![2, 4]]),
            1
        );
    }
}
