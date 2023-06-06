// 48.4.1
let rec fibo1 n n1 n2 = match n with
  | 0 -> n2
  | 1 -> n1
  | n -> fibo1 (n - 1) (n1 + n2) n1
  
// 48.4.2
let rec fibo2 n f = match n with
  | 0 -> f 0
  | 1 -> f 1
  | n -> fibo2 (n - 2) (fun a -> fibo2 (n - 1) (fun b -> f (a + b)))

// 48.4.3
let rec bigList n k =
  if n=0 then k []
  else bigList (n-1) (fun res -> k(1::res))
