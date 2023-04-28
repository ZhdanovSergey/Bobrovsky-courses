// 17.1
let rec pow = function
  | (s,n) when n <= 0 -> ""
  | (s,n) -> s + pow(s,n-1)
  
// 17.2
let isIthChar = function
  | (s,n,c) when n < 0 || n >= (String.length s) -> false
  | (s,n,c) -> s.[n] = c

// 17.3
let rec occFromIth = function
  | (s,n,c) when n >= (String.length s) -> 0
  | (s,n,c) when n < 0 -> occFromIth(s,0,c)
  | (s,n,c) when s.[n] = c -> 1 + occFromIth(s,n+1,c)
  | (s,n,c) when not (s.[n] = c) -> occFromIth(s,n+1,c)
