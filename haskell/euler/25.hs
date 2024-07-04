module Main where

  f :: Int -> Int -> Int -> Int
  f a b k
    | length (show b) >= 1000 = k - 1
    | otherwise = f b (a + b) (k + 1)

  main :: IO ()
  main =
    print (f 1 1 3)