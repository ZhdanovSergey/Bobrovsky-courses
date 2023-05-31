// 42.3
let rec allSubsets n k = match (n, k) with
  | (n, k) when n < k || k = 0 -> Set.empty
  | (n, k) when n >= k -> Set.union (allSubsets (n - 1) k) (Set.map (fun x -> Set.add n x) (allSubsets (n - 1) (k - 1)))
  
printfn "%A" (allSubsets 0 0)
