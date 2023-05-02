let curry f x y = f(x,y)

let uncurry f = fun (x,y) -> f(x)(y)
