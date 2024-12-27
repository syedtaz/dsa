pub struct Solution {}

impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let mut i = 0;
        let mut j = arr.len() - (k as usize);

        while i < j {
            let mid = i + (j - i) / 2;
            if x - arr[mid] > arr[mid + k as usize] - x {
                i = mid + 1;
            } else {
                j = mid;
            }
        }

        arr[i..(i + k as usize)].into()
    }
}
#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn example1() {
        assert_eq!(
            Solution::find_closest_elements(vec![1, 2, 3, 4, 5], 4, 3),
            vec![1, 2, 3, 4]
        );
    }
}
