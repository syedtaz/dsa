pub struct Solution {}

impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        #[inline(always)]
        fn char_code(x: &char) -> usize {
            match x {
                'a' => 1,
                'e' => 2,
                'i' => 4,
                'o' => 8,
                'u' => 16,
                _ => 0,
            }
        }

        let mut pref: usize = 0;
        let mut idxs = [-1; 32];
        let mut acc = 0;

        for (i, c) in s.chars().enumerate() {
            pref = pref ^ char_code(&c);
            if idxs[pref] == -1 && pref != 0 {
                idxs[pref] = i as i32;
            }
            acc = acc.max(i as i32 - idxs[pref])
        }

        acc
    }
}
