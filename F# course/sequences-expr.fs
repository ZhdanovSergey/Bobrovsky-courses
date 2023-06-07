// 50.2.1
let rec fac n res = seq {
  yield res
  yield! fac (n + 1) (res * (n + 1))
}

let fac_seq = seq {
  yield 1
  yield! seq (fac 1 1)
}

// 50.2.2
let rec f i = seq {
  yield (0 - i)
  yield i
  yield! f(i + 1)
}
  
let seq_seq = seq {
  yield 0
  yield! f 1
}
