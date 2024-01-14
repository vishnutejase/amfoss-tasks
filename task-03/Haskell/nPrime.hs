isPrime :: Int -> Bool
isPrime num
    | num < 2 = False
    | otherwise = all (\x -> num `mod` x /= 0) [2..truncate $ sqrt $ fromIntegral num]

findPrimes :: Int -> [Int]
findPrimes n = filter isPrime [2..n]

main :: IO ()
main = do
    putStrLn "Enter a number: "
    n <- readLn
    let result = findPrimes n
    putStrLn $ "Prime numbers up to " ++ show n ++ " are: " ++ show result
