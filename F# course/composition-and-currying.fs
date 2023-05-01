// 20.3.1
let vat (n: int) (x: float): float = x * (1.0 + float(n) / 100.0)

// 20.3.2
let unvat (n: int) (x: float): float = x / (1.0 + float(n) / 100.0)

// 20.3.3
let rec minAcc (f,n) = if f(n) = 0 then n else minAcc(f,n+1)
let min f = minAcc(f,1)