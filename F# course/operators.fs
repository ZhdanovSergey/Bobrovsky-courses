// 16.1
let notDivisible (n,m) = m % n = 0

let rec primeRec = function
  | (n,1) -> true
  | (1,m) -> true
  | (n,m) -> not (notDivisible(n,m)) && (primeRec(n-1, m))

// 16.2
let prime n = primeRec(n-1, n)