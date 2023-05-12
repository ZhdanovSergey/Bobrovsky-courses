// 34.1
let upto n =
  let rec uptoRec = function
    | (k, acc) when k <= 0 -> acc
    | (k, acc) -> uptoRec(k-1, k :: acc)
  uptoRec(n, [])
  
// 34.2
let dnto n =
  let rec dntoRec = function
    | (k, acc) when k > n -> acc
    | (k, acc) -> dntoRec(k+1, k :: acc)
  dntoRec(1, [])
  
// 34.3
let evenn n =
  let rec evennRec = function
    | (k, acc) when k < 0 -> acc
    | (k, acc) -> evennRec(k-2, k :: acc)
  evennRec((n-1)*2, [])
