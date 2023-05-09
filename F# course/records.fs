type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y = (x.f, x.hours, x.minutes) > (y.f, y.hours, y.minutes)
