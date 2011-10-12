
fibonacci :: (Num a) => a -> a
fibonacci x
  | x == 0 = x
  | x == 1 = x
  | otherwise = fibonacci (x - 1) + fibonacci (x - 2)
