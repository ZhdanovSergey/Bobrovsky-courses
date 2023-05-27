// 40.1
let rec sum (p, xs) = match xs with
  | [] -> 0
  | head :: tail when (p head) -> head + sum(p, tail)
  | head :: tail -> sum(p, tail)

// 40.2.1
let rec count (xs, n) = match xs with
  | head :: tail when head < n -> count(tail, n)
  | head :: tail when head = n -> 1 + count(tail, n)
  | _ -> 0

// 40.2.2
let rec insert (xs, n) = match xs with
  | [] -> [n]
  | head :: tail when n <= head -> n :: head :: tail
  | head :: tail -> head :: insert(tail, n)
  
// 40.2.3
let rec intersect = function
  | (xs1, []) -> []
  | ([], xs2) -> []
  | (head1 :: tail1, head2 :: tail2) when head1 < head2 -> intersect(tail1, head2 :: tail2)
  | (head1 :: tail1, head2 :: tail2) when head1 > head2 -> intersect(head1 :: tail1, tail2)
  | (head1 :: tail1, head2 :: tail2) -> head1 :: intersect(tail1, tail2)
  
// 40.2.4
let rec plus = function
  | (xs1, []) -> xs1
  | ([], xs2) -> xs2
  | (head1 :: tail1, head2 :: tail2) when head1 < head2 -> head1 :: plus(tail1, head2 :: tail2)
  | (head1 :: tail1, head2 :: tail2) -> head2 :: plus(head1 :: tail1, tail2)

// 40.2.5  
let minus (xs1, xs2) =
  let rec iter (xs1, xs2, result) = match (xs1, xs2) with
    | (xs1, []) -> result @ xs1
    | ([], xs2) -> result
    | (head1 :: tail1, head2 :: tail2) when head1 < head2 -> iter(tail1, head2 :: tail2, result @ [head1])
    | (head1 :: tail1, head2 :: tail2) when head1 > head2 -> iter(head1 :: tail1, tail2, result)
    | (head1 :: tail1, head2 :: tail2) -> iter(tail1, tail2, result)
  iter(xs1, xs2, [])

// 40.3.1
let rec smallest = Some(0)

// 40.3.2
let rec delete (n, xs) = []

// 40.3.3
let rec sort = []

// 40.4
let rec revrev = []
