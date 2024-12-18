pub struct Solution {}

impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let mut times: Vec<i32> = time_points
            .into_iter()
            .map(|x| {
                let split: Vec<i32> = x.split(":").map(|x| x.parse::<i32>().unwrap()).collect();
                split[0] * 60 + split[1]
            })
            .collect();

        times.sort();
        let candidate = times
            .iter()
            .zip(times.iter().skip(1))
            .fold(u32::MAX, |acc, (a, b)| acc.min(a.abs_diff(*b))) as i32;
        candidate.min(24 * 60 - times.last().unwrap() + times.first().unwrap())
    }
}
