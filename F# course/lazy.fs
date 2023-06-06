// 48.4.1
let rec fibo1 n n1 n2 = match n with
  | 0 -> n2
  | 1 -> n1
  | n -> fibo1 (n - 1) (n1 + n2) n1
