// 41.4.1
let list_filter f xs =
  let filter x acc = if (f x) then x :: acc else acc
  List.foldBack filter xs []
