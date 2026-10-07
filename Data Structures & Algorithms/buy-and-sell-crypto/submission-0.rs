impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {

        let mut min_price = prices[0];
        let mut profit  = 0;

        for i in 1..prices.len() {

            let today_profit = prices[i] - min_price;
            profit = profit.max(today_profit);
            min_price = min_price.min(prices[i])
        }

        profit

    }
}
