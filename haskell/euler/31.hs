module Main where

denoms :: [Int]
denoms = [1, 2, 5, 10, 20, 50, 100, 200]

coinChange :: Int -> Int -> Int
coinChange 1 _ = 1
coinChange l num =
  sum $ map f [0 .. num `div` (denoms !! pred l)]
  where
    f x = coinChange (pred l) (num - x * (denoms !! pred l))

main :: IO ()
main =
  print (coinChange (length denoms) 200)