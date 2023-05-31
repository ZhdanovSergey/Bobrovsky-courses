// 42.3
let rec allSubsets n k = match (n, k) with
  | (n, k) when n < k -> Set.empty
  | (n, 0) -> set [Set.empty]
  | (n, k) ->
    let add_n subset = Set.add n subset
    Set.union (allSubsets (n - 1) k) (Set.map add_n (allSubsets (n - 1) (k - 1)))
