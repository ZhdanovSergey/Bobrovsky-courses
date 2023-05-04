open System

// 23.4.1
let (.+.) x y =
  let (x1,x2,x3) = x
  let (y1,y2,y3) = y
  let res3 = x3 + y3
  let res2 = x2 + y2 + res3 / 12
  let res1 = x1 + y1 + res2 / 20
  res1, res2 % 20, res3 % 12
  
let (.-.) x y =
  let (x1,x2,x3) = x
  let (y1,y2,y3) = y
  let res3 = x3 - y3
  let diff2 = if res3 < 0 then int(System.Math.Ceiling(float(-res3) / 12.0)) else 0
  let res2 = x2 - y2 - diff2
  let diff1 = if res2 < 0 then int(System.Math.Ceiling(float(-res2) / 20.0)) else 0
  let res1 = x1 - y1 - diff1
  res1, res2 + diff1 * 20, res3 + diff2 * 12
