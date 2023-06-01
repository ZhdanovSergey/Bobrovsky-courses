// 43.3
let rec search (list, key) = 
  match list with 
    | (k, v) :: tail when k = key -> Some(v) 
    | (k, v) :: tail -> search (tail, key) 
    | [] -> None
let try_find key m = search (Map.toList m, key)
