// 49.5.1
let even_seq = Seq.initInfinite (fun n -> 2 * (n + 1))

// 49.5.2
let fac_seq = Seq.initInfinite (fun n -> List.fold (*) 1 [1..n])

// 49.5.3
let seq_seq = Seq.initInfinite (fun n -> if n % 2 = 0 then (n+1)/2 else -(n+1)/2)
