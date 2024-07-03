module Main where
  main =
    do
      content <- readFile "13"
      print (trunc $ f content)
    where
      f :: String -> Integer
      f s = sum $ map (\x -> read x :: Integer) (lines s)

      trunc :: Integer -> Integer
      trunc num =
        let n = length $ show num in
        num `div` (10 ^ (n - 10))

