pub struct Solution {}

impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut p = 0;
        let mut i = 0;
        let mut j = 1;
        let mut word = String::with_capacity(3);

        while i < chars.len() {
            let mut count = 1;
            while j < chars.len() && chars[j] == chars[i] {
                j += 1;
                count += 1;
            }

            match count {
                1 => {
                    chars[p] = chars[i];
                    p += 1;
                }
                _ => {
                    chars[p] = chars[i];
                    word.clear();
                    word.push_str(&count.to_string());
                    let buf = word.as_bytes();
                    for (i, v) in buf.iter().enumerate() {
                        chars[p + i + 1] = *v as char;
                    }
                    p += buf.len() + 1;
                }
            }
            i = j;
            j += 1;
        }

        p as i32
    }
}
