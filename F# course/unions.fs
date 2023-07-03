type F = 
  | AM
  | PM

type TimeOfDay = { hours : int; minutes : int; f: F }

let (.>.) x y = (x.f, x.hours, x.minutes) > (y.f, y.hours, y.minutes)
