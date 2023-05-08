let rec iter = function
    | (a, b, c) when c > 11 -> iter (a, b + (c / 12), c % 12)
    | (a, b, c) when b > 19 -> iter (a + (b / 20), b % 20, c)
    | (a, b, c) when c < 0 && b > 0 -> iter (a, b - 1, c + 12)
    | (a, b, c) when b < 0 && a > 0 -> iter (a - 1, b + 20, c)
    | (a, b, c) when c < 0 && a > 0 -> iter (a - 1, b + 19, c + 12)
    | (a, b, c) -> (a, b, c)

let (.+.) (a, b, c) (x, y, z) = iter (a + x, b + y, c + z)
let (.-.) (a, b, c) (x, y, z) = iter (a - x, b - y, c - z)

let (.+) (a, b) (c, d) = (a + c, b + d)
let (.-) (a, b) (c, d) = (a - c, b - d)
let (.*) (a, b) (c, d) = (a * c - b * d, b  * c + a * d)
let (./) (a, b) (c, d) = (a, b) .* (c / (c * c + d * d) , -d / (c * c + d * d))
