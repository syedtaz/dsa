#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices
            .iter()
            .fold((prices[0], 0), |(min_price, max_profit), price| {
                let temp = min_price.min(*price);
                (temp, max_profit.max(price - temp))
            })
            .1
    }
}
