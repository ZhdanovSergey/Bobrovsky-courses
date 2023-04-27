// 17.1
let rec pow = function
  | (s,1) -> s
  | (s,n) -> s + pow(s,n-1)
  
// 17.2
let rec isIthChar = fun (s: string, n: int ,c: char) -> s.[n] = c

// 17.3
let rec occFromIth = function
  | (s,n,c) when (String.length s) = n -> 0
  | (s,n,c) when s.[n] = c -> 1 + occFromIth(s,n+1,c)
  | (s,n,c) when not (s.[n] = c) -> occFromIth(s,n+1,c)