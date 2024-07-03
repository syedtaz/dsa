module Main where

square x = x * x

sumSquare n = sum $ map square $ take n [1 ..]

squareSum n = square $ sum $ take n [1 ..]

main :: IO ()
main = do
  print (sumSquare 100 - squareSum 100)
