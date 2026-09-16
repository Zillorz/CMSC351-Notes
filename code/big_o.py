# this function can only calculate the following O(g(n))
# g(n) = x, x^2 ... x^9, e^x, log(x), x * log(x), x^2 * log(x)
import random
import time
import math
from typing import Any, Callable


def mechanical_big_o(measure: Callable[[int], Any]):
    # 4, 5, 6, 7
    times: list[float] = []

    iterations = 6
    start = 5
    growth_factor = 2
    reps = 100000

    # warm up
    for i in range(1, 3):
        _ = measure_avg(measure, start * growth_factor, reps)

    # base = measure_avg(measure, 1, 100)

    for i in range(iterations):
        times.append(
                measure_avg(measure, start * round(math.pow(growth_factor, i)), reps)
        )

    m, c = regression(reduction(times))

    print(round(m, 4))
    print(round(c, 4))

# if we have f(n) = c, f(2n) = f(n)
# if we have f(n) = lg n, f(cn) = A + f(n)
# if we have f(n) = n, f(2n) = 2f(n)
# if we have f(n) = n^a, f(2n) = 2^a * f(n)
# if we have f(n) = n^a * lg(n), f(2n) = C + 2^a * f(n)

# at this point, single reduction is no longer useful

# if we have f(n) = a^x, f(2n) = a^(2x) = f(n) * f(n) 
# if we have f(n) = n!, f(2n) = (2n)! which is too difficult to measure like this
# if we have f(n) = n^n, f(2n) = (2n)^2n, which is too difficult to measure like this

def reduction(inp: list[float]) -> list[float]:
    out: list[float] = []

    for i in range(len(inp) - 1):
        out.append(inp[i + 1] / inp[i])

    return out

# see linear regression formula
def regression(inp: list[float]) -> tuple[float, float]:
    n = float(len(inp))

    tsum = 0 # times sum, x * y
    sum = 0 # sum of y
    lsum = (n * (n + 1)) / 2 # sum of x
    ssum = lsum * (2 * n + 1) / 3 # sum of x^2
    
    for i, y in enumerate(inp):
        x = i + 1
        tsum += x * y
        sum += y

    slope = (n * tsum - lsum * sum) / (n * ssum - lsum * lsum)
    const = (sum - slope * lsum) / n

    return slope, const

def measure_avg(measure: Callable[[int], Any], n: int, reps: int=10):
    time_sum = 0

    for _ in range(reps):
        start = time.perf_counter()
        _ = measure(n)
        end = time.perf_counter()

        time_sum += end - start

    time_sum /= reps
    return time_sum


# this is our function which measures time
def skinny_function(n: int):
    func: Callable[[int], int] = lambda x: x * x * round(math.log(x))

    for _ in range(func(n)):
        time.sleep(0.000001)

def rsum(n: int):
    a = [random.randint(1, 20) for _ in range(n)]
    s = 0

    for v in a:
        s += v

    return s 

mechanical_big_o(rsum)
