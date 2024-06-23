#![allow(dead_code)]

struct Solution;

#[inline(always)]
pub fn roman_map(x: char) -> i32 {
    match x {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
        _ => panic!(),
    }
}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        if s.len() == 0 {
            return 0;
        }

        let mut acc: i32 = 0;

        for (prev, cur) in s
            .chars()
            .zip(s.chars().skip(1))
            .map(|(a, b)| (roman_map(a), roman_map(b)))
        {
            acc += cur;
            if prev < cur {
                acc -= 2 * prev;
            }
        }

        acc + roman_map(s.chars().nth(0).unwrap())
    }
}
