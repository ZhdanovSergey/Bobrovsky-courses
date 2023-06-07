// 50.2.1
let fac_seq = seq {
  yield! (Seq.initInfinite (fun n -> List.fold (*) 1 [1..n]))
}

// 50.2.2
let seq_seq = seq {
  yield! (Seq.initInfinite (fun n -> if n % 2 = 0 then (n+1)/2 else -(n+1)/2))
}
