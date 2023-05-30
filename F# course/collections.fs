// 41.4.1
let list_filter f xs =
  let filter x acc = if (f x) then x :: acc else acc
  List.foldBack filter xs []

// 41.4.2
let sum (p, xs) =
  let sum_step acc x = if (p x) then x + acc else acc
  List.fold sum_step 0 xs
  
// 41.4.3
let revrev xs =
  let rev_step acc x = x :: acc
  let revrev_step acc x = (List.fold rev_step [] x) :: acc
  List.fold revrev_step [] xs
