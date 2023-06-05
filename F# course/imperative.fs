// 47.4.1
let f n =
  let mutable result = 1
  let iterStep x = result <- result * x
  List.iter iterStep [1 .. n]
  result

// 47.4.2
let fibo n = if n = 0 || n = 1 then n else
  let mutable i = 2
  let last2Fibos = [| 0; 1 |]
  while i <= n do
    let nextFibo = last2Fibos.[0] + last2Fibos.[1]
    last2Fibos.[0] <- last2Fibos.[1]
    last2Fibos.[1] <- nextFibo
    i <- i + 1
  last2Fibos.[1]
