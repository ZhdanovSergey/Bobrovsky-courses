// 39.1
let rec rmodd = function
  | head :: (head2 :: tail) -> head2 :: rmodd tail
  | _ -> []

// 39.2
let rec del_even = function
  | [] -> []
  | head :: tail when head % 2 = 0 -> del_even tail
  | head :: tail -> head :: del_even tail
  
// 39.3
let multiplicity x xs =
  let rec iter (list, i) = match list with
    | [] -> i
    | head :: tail when head = x -> iter(tail, i+1)
    | head :: tail -> iter(tail, i)
  iter(xs, 0)
  
// 39.4
let rec rmodd2 = function
  | head :: (head2 :: tail) -> head :: rmodd2 tail
  | [head] -> [head]
  | _ -> []

let rec split = fun xs -> (rmodd2 xs, rmodd xs)
  
// 39.5
let rec zip (xs1,xs2) =
  if List.length xs1 <> List.length xs2
    then failwith "The lists are of different length"
    else match (xs1, xs2) with
      | ([], []) ->  []
      | (head1 :: tail1, head2 :: tail2) -> (head1, head2) :: zip(tail1, tail2)
