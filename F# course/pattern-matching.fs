let days_in_month = function
  | 2 -> 28
  | 4|6|9|11 -> 30
  | 1|3|5|7|8|10|12 -> 31
  | _ -> 0