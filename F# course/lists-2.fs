// 39.1
let rmodd list =
  let rec rmoddRec = function
    | ([], acc) -> acc
    | (list, acc) when (List.length acc) % 2 = 0 -> rmoddRec(list, 0 :: acc)
    | (head :: tail, acc) -> rmoddRec(tail, head :: acc)
  
  List.rev (rmoddRec(list, []))
  
// 39.2
let del_even list =
  let rec del_even_rec = function
    | ([], acc) -> acc
    | (head :: tail, acc) when head % 2 = 0 -> del_even_rec(tail, acc)
    | (head :: tail, acc) -> del_even_rec(tail, head :: acc)
  
  List.rev (del_even_rec(list, []))
  
// 39.3
let multiplicity value list =
  let rec multiplicity_rec = function
    | ([], counter) -> counter
    | (head :: tail, counter) when head = value -> multiplicity_rec(tail, counter + 1)
    | (head :: tail, counter) -> multiplicity_rec(tail, counter)
  
  multiplicity_rec(list, 0)
  
// 39.4
let split list =
  let rec split_rec = function
    | ([], evenList, oddList) -> (evenList, oddList)
    | ([lastElem], evenList, oddList) -> (lastElem :: evenList, oddList)
    | (even_head :: odd_head :: tail, evenList, oddList) -> split_rec(tail, even_head :: evenList, odd_head :: oddList)
  
  let (evenList, oddList) = split_rec(list, [], [])
  (List.rev evenList, List.rev oddList)
  
// 39.5
exception DifferentLengths
let zip (list1, list2) =
  let rec zip_rec = function
    | (list1, list2, []) when (List.length list1) <> (List.length list2) -> raise DifferentLengths
    | ([], [], acc) -> acc
    | (head1 :: tail1, head2 :: tail2, acc) -> zip_rec(tail1, tail2, (head1, head2) :: acc)
  
  List.rev (zip_rec(list1, list2, []))
